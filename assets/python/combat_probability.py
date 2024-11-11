from icepool import map, d, Die
import numpy as np
from scipy.special import erf
import plotly.graph_objects as go

def gaussian(mu, sigma, d):
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((d - mu)/(sigma))**2)

def gaussian_cdf(mu, sigma, d):
    if sigma > 0:
        return 1 - 0.5*(1 + erf((d - mu)/(sigma*np.sqrt(2))))
    elif d >= mu:
        return 0.0
    else:
        return 1.0

def gaussian_fit(damage, method='default'):
    """takes a damage distribution and returns the r-squared for how well 
    it fits a gaussian distribution with the same mean and sigma.
    """
    sigma = damage.standard_deviation()
    mean = damage.mean()
    match method:
        case 'range':
            dmin = np.round(mean - 4*sigma, 0)
            dmax = np.round(mean + 4*sigma, 0)
            dx = np.linspace(dmin, dmax, int(1 + dmax - dmin)).astype(int)
        case 'bottom-half':
            dmin = np.round(mean - 4*sigma, 0)
            dmax = np.round(mean, 0)
            dx = np.linspace(dmin, dmax, int(1 + dmax - dmin)).astype(int)
        case 'top-half':
            dmin = np.round(mean, 0)
            dmax = np.round(mean + 4*sigma, 0)
            dx = np.linspace(dmin, dmax, int(1 + dmax - dmin)).astype(int)
        case _:
            dx = np.array(damage.outcomes())

    dp = np.array([damage.probability(d) for d in dx])
    gp = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((dx - mean)/(sigma))**2)

    rss = np.square(dp - gp).sum()
    tss = np.square(dp - dp.mean()).sum()
    r2 = 1 - rss/tss

    return gp, r2

def rounds_to_gaussian(damage, rsquared=0.95, method='default'):
    r = 0
    rsq = 0
    while rsq < rsquared:
        r += 1
        _, rsq = gaussian_fit(r @ damage, method)
    return r


def save_damage(n_targets, targets_roll, fail_damage_roll, save_factor):
    """Used to convert the distribution of saving throw failures for a given number of targets into the total damage.
    """
    return fail_damage_roll*targets_roll + (n_targets - targets_roll)*success_damage(save_factor, fail_damage_roll)

def success_damage(factor, fail_damage_roll):
    """Converts the damage done on a failed save to damage on a successful save.
    """
    return np.floor(factor*fail_damage_roll)

def saving_throw_fails(save_bonus, save_roll, difficulty_class):
    """Used to determine the probability distribution of failed saves and successful ones.
    """
    if save_roll + save_bonus >= difficulty_class:
        return 0.0
    else:
        return 1.0

class save:
    def __init__(self, dc, fail_damage, save_factor):
        self.dc = dc
        self.fail_damage = fail_damage
        self.save_factor = save_factor
    
    def damage(self, save_bonus, n_targets):
        """Calculates the distribution of total damage done by the saving throw against a set number of targets.
        """
        st = n_targets @ map(saving_throw_fails, save_bonus, d(20), self.dc)
        return map(save_damage, n_targets, st, self.fail_damage, self.save_factor)


def attack_damage(armor_class, attack_roll, attack_bonus, hit_damage_roll, crit_damage_roll):
    if attack_roll == 20:
        return crit_damage_roll
    elif attack_roll == 1:
        return 0
    elif attack_roll + attack_bonus >= armor_class:
        return hit_damage_roll
    else:
        return 0

class attack:
    def __init__(self, ab, hit_damage, crit_damage):
        self.ab = ab
        self.hit_damage  = hit_damage
        self.crit_damage = crit_damage

    def damage(self, armor_class):
        return map(attack_damage, armor_class, d(20), self.ab, self.hit_damage, self.crit_damage)


class Combatant:
    def __init__(self, **kwargs):
        self.group = kwargs.get('group', None)
        self.name = kwargs.get('name', None)
        self.opponent = kwargs.get('opponent', None)
        self.level = kwargs.get('level', None)
        self.hit_points = kwargs.get('hit_points', None)
        self._dpr = kwargs.get('damage', [])
        self.round = 0
    
    def dpr(self, round):
        return self._dpr[round % len(self._dpr) - 1]
    
    def damage(self, round):
        if round == 0:
            return Die({0: 1})
        else:
            return sum([self.dpr(r) for r in range(1, round+1)])

def gaussian_dice_distribution(mean, sigma):
    """Creates a die that follows the gaussian distribution defined by
    the given mean and sigma.
    """
    n_sigmas = 6
    #d_min = max(np.floor(mean - n_sigmas*sigma), 1)
    d_min = np.floor(mean - n_sigmas*sigma)
    d_max = np.floor(mean + n_sigmas*sigma)
    d_vals = np.linspace(d_min, d_max, int(d_max - d_min + 1)).astype(int)
    d_probs = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((d_vals - mean)/(sigma))**2)
    d_weights = np.round(d_probs/min(d_probs)).astype(int)

    return Die({int(d): int(p) for d, p in zip(d_vals, d_weights)})

def gaussian_die_approximation(dice):
    """Creates a die that follows the gaussian distribution defined by
    the given mean and sigma.
    """
    return gaussian_dice_distribution(dice.mean(), dice.sd())

def baseline_monster(cr, **kwargs):
    dpr_mean = (6 + 6*cr)*kwargs.get('prob', 0.65)
    dpr_sigma = dpr_mean*kwargs.get('CV', 0.4)
    return Combatant(
        group = kwargs.get('group', 'monsters'),
        name = kwargs.get('name', 'Mon'),
        opponent = kwargs.get('opponent', 'player characters'),
        level = cr,
        hit_points = 1*(16 + 16*cr),
        damage = [gaussian_dice_distribution(dpr_mean, dpr_sigma)],
    )

def baseline_player_character(level, **kwargs):
    dpr_mean = (7 + 2*level)*kwargs.get('prob', 0.65)
    dpr_sigma = dpr_mean*kwargs.get('CV', 0.4)
    return Combatant(
        group = kwargs.get('group', 'player characters'),
        name = kwargs.get('name', 'PC'),
        opponent = kwargs.get('opponent', 'monsters'),
        level = level,
        hit_points = (1 + 7*level),
        damage = [gaussian_dice_distribution(dpr_mean, dpr_sigma)],
    )


def safe_add(threshold, d1, d2):
    d = d1 + d2
    if d > threshold:
        d = threshold
    return d

def safe_add_2(threshold, d1, d2):
    if d1 >= threshold:
        return d1
    else:
        return d1 + d2

def split_overdamage(dmg, threshold):
    du = Die({k: q for k, q in dmg.items() if k <  threshold})
    do = Die({k: q for k, q in dmg.items() if k >= threshold})

    if du.is_empty(): du = Die({0:1})
    if do.is_empty(): do = Die({0:1})

    return du, do

class Encounter:
    def __init__(self, combatants, **kwargs):
        self.combatants = combatants

        self.__initiative(**kwargs)

        self.__construct_groups()

        self.__construct_turns(**kwargs)
    
    def __initiative(self, **kwargs):
        """Orders the combatants according to the initiative order given. 
        
        The order lists the combatants names in the order they take their turns and should have one entry per combatant. 
        """
        if 'initiative' in kwargs:
            self.initiative = kwargs['initiative']
            self.combatants = [self.get_combatant(name) for name in self.initiative]
        else:
            self.initiative = [c.name for c in self.combatants]

    def __construct_groups(self):
        group_names = list(set([c.group for c in self.combatants]))
        groups = {}
        for g in group_names:
            groups[g] = {
                'opponent': [c.opponent for c in self.combatants if c.group == g][0],
                'damage': 0,
                'hit points': sum([c.hit_points for c in self.combatants if c.group == g]),
                'win probability': 0,
            }
        self.groups = groups

    def __construct_turns(self, **kwargs):
        turns = [
            {
                'turn': 0,
                'round': 0, 
                'name': None, 
                'group': None,
            }
        ]
        t = 0
        for r in range(1, 1 + kwargs.get('rounds', 10)):
            for c in self.combatants:
                t += 1
                turns += [{
                    'turn': t,
                    'round': r, 
                    'name': c.name, 
                    'group': c.group,
                }]
        self.turns = turns

    def combatant_turns_mean(self, **kwargs):
        """Returns the average number of turns taken by each combatant in the encounter.
        """
        turns_count = {c.name: 0 for c in self.combatants}
        turns_mean = {c.name: 0 for c in self.combatants}
        win_probs = self.encounter_win_pdf(**kwargs)
        for t, p in zip(self.turns, win_probs):
            if not t['name']: continue
            turns_count[t['name']] += 1
            for k, v in turns_count.items():
                turns_mean[k] += p*v

        return turns_mean
    
    def combatant_turns_sigma(self, **kwargs):
        """Returns the standard deviation of the number of turns taken by each combatant in the encounter.
        """
        turns_variance = self.combatant_turns_variance(**kwargs)
        return {k: np.sqrt(v) for k, v in turns_variance.items()}
    
    def combatant_turns_variance(self, **kwargs):
        """Returns the variance of the number of turns taken by each combatant in the encounter.
        """
        turns_mean = self.combatant_turns_mean(**kwargs)
        turns_count = {c.name: 0 for c in self.combatants}
        turns_variance = {c.name: 0 for c in self.combatants}
        win_probs = self.encounter_win_pdf(**kwargs)
        for t, p in zip(self.turns, win_probs):
            if not t['name']: continue
            turns_count[t['name']] += 1
            for k, v in turns_count.items():
                turns_variance[k] += p*(v - turns_mean[k])**2

        return turns_variance

    def encounter_win_cdf(self, **kwargs):
        """Returns the cumulative probability the encounter ends during each turn
        or before.
        """
        return list(np.cumsum(self.encounter_win_pdf(**kwargs)))
    
    def encounter_length(self, **kwargs):
        """Returns the average length of the encounter in turns or rounds."""
        win_pdf = self.encounter_win_pdf(**kwargs)
        turns = sum([t*win_pdf[t] for t in range(len(win_pdf))])
        units = kwargs.get('units', 'round').lower()
        if units in ['round','rounds']:
            return turns/len(self.combatants)
        elif units in ['turn','turns']:
            return turns
        else:
            raise('Unrecognized unit!')
    
    def encounter_length_sigma(self, **kwargs):
        """Returns the standard deviation in the length of the encounter in turns or rounds."""
        return np.sqrt(self.encounter_length_variance(**kwargs))

    def encounter_length_variance(self, **kwargs):
        """Returns the variance in the length of the encounter in turns or rounds."""
        turns_mean = self.encounter_length(units='turns')

        win_pdf = self.encounter_win_pdf(**kwargs)
        turns = sum([((t - turns_mean)**2) *win_pdf[t] for t in range(len(win_pdf))])
        units = kwargs.get('units', 'round').lower()
        if units in ['round','rounds']:
            return turns/(len(self.combatants)**2)
        elif units in ['turn','turns']:
            return turns
        else:
            raise('Unrecognized unit!')
        
    def encounter_win_pdf(self, **kwargs):
        """Returns the probability the encounter ends during each turn
        """
        pdf = np.zeros(len(self.turns))
        for group_name in self.groups:
            pdf = pdf + np.array(self.group_win_pdf(group_name, **kwargs))
        return list(pdf)

    def get_combatant(self, name):
        for c in self.combatants:
            if c.name == name:
                return c
        return None
    
    def get_turn(self, name, round):
        for t in self.turns:
            if name == t['name'] and round == t['round']:
                return t['turn']
        return None

    def group_damage_cdf(self, group_name, **kwargs):
        """Returns the probability of the given group having dealt enough 
        damage to defeat their opponent for each turn.
        """

        if kwargs.get('method', 'exact') == 'approx':
            return self.group_damage_cdf_approx(group_name)
        else:
            return self.group_damage_cdf_exact(group_name)
    
    def group_damage_cdf_exact(self, group_name):
        """Returns the probability of the given group having dealt enough 
        damage to defeat their opponent for each turn.
        """
        damage = Die({0: 1})
        opponent = self.groups[group_name]['opponent']
        opponent_hit_points = self.groups[opponent]['hit points']
        cdf = []
        for t in self.turns:
            if t['group'] == group_name:
                c = self.get_combatant(t['name'])
                damage = damage + c.dpr(t['round'])
            cdf += [(damage >= opponent_hit_points).mean()]
        return cdf
    
    def group_damage_cdf_approx(self, group_name):
        """Returns the probability of the given group having dealt enough 
        damage to defeat their opponent for each turn.
        """
        damage_mean = 0
        damage_var = 0
        opponent = self.groups[group_name]['opponent']
        opponent_hit_points = self.groups[opponent]['hit points']
        cdf = []
        for t in self.turns:
            if t['group'] == group_name:
                c = self.get_combatant(t['name'])
                damage_mean += c.dpr(t['round']).mean()
                damage_var += c.dpr(t['round']).variance()

            cdf += [gaussian_cdf(damage_mean, np.sqrt(damage_var), opponent_hit_points - 0.5)]
        return cdf
    
    def group_damage_pdf(self, group_name, **kwargs):
        """Returns the probability of the given group dealing enough 
        damage to defeat their opponent during each turn.
        """
        cdf = self.group_damage_cdf(group_name, **kwargs)
        return [0.0] + [cdf[i] - cdf[i-1] for i in range(1, len(cdf))]
    
    def group_damage(self, group_name, turn, **kwargs):
        """Returns the damage distribution for the given group at the end of the given turn.
        """
        """
        damage = Die({0: 1})
        for t in self.turns[0:turn]:
            if t['group'] == group_name:
                damage += self.get_combatant(t['name']).dpr(t['round'])
        """
        turns = [t for t in self.turns if t['turn'] <= turn and t['group'] == group_name]
        damage = Die({0: 1}) + sum([self.get_combatant(t['name']).dpr(t['round']) for t in turns])

        if kwargs.get('clip', False):
            opponent = self.groups[group_name]['opponent']
            damage = damage.clip(max_outcome=self.groups[opponent]['hit points'])

        return damage
    
    def group_damage_old(self, group_name, round, **kwargs):
        """Returns the damage distribution for the given group at the end of rounds of combat.
        """
        turns = [t for t in self.turns if t['round'] <= round and t['group'] == group_name]
        damage = Die({0: 1}) + sum([self.get_combatant(t['name']).dpr(t['round']) for t in turns])
        
        if kwargs.get('clip', False):
            opponent = self.groups[group_name]['opponent']
            damage = damage.clip(max_outcome=self.groups[opponent]['hit points'])

        return damage
    
    def group_damage_distribution(self, group_name, **kwargs):
        """returns the final damage distribution for the given group.

        This is an attempt to fix the problem with the older version of this function.
        This version is always "clipped", gotta figure out how to handle a non-clipped version ...
        """
        
        # get the wights for the damage from each round
        win_probs = np.array(self.encounter_win_pdf())

        damage_dict = {}
        for t, p in zip(self.turns, win_probs):
            if p == 0:
                continue
            
            damage, over_damage = self.group_overdamage(group_name, t['turn'])
            if t['group'] == group_name:
                for k, v in zip(over_damage.keys(), over_damage.probabilities()):
                    damage_dict[k] = damage_dict.get(k, 0) + p*v
            else:
                for k, v in zip(damage.keys(), damage.probabilities()):
                    damage_dict[k] = damage_dict.get(k, 0) + p*v

        # convert to die
        for k, v in damage_dict.items():
            damage_dict[k] = int(v*1.0e8)
        damage = Die(damage_dict)

        if kwargs.get('clip', False):
            opponent = self.groups[group_name]['opponent']
            damage = damage.clip(max_outcome=self.groups[opponent]['hit points'])

        return damage
    
    def group_damage_mean(self, group_name, **kwargs):
        """returns the average final damage for the given group.
        """
        method = kwargs.get('method', 'exact')
        if method == 'approx':
            return self.group_damage_mean_approx(group_name, **kwargs)
        else:
            return self.group_damage_distribution(group_name, **kwargs).mean()

    def group_damage_mean_approx(self, group_name, **kwargs):
        """returns the average final damage for the given group.
        """
        clip = kwargs.get('clip', False)

        cdf = self.group_damage_cdf_approx(group_name)
        opponent = self.groups[group_name]['opponent']
        opponent_hit_points = self.groups[opponent]['hit points']

        d_ave = []
        damage_mean = 0
        damage_var = 0
        win_probs = np.array(self.encounter_win_pdf(**kwargs))
        for i in range(len(self.turns)):
            t = self.turns[i]
            if t['group'] == group_name:
                c = self.get_combatant(t['name'])
                damage_mean += c.dpr(t['round']).mean()
                damage_var += c.dpr(t['round']).variance()
                if clip:
                    d_ave_turn = opponent_hit_points
                else:
                    d_ave_turn = damage_mean
            else:
                d_ave_turn = 0
                if (damage_mean > 0) and (cdf[i] < 1):
                    d_ave_turn += damage_mean - damage_var*gaussian(damage_mean, np.sqrt(damage_var), opponent_hit_points - 0.5)/(1 - cdf[i])
            
            d_ave += [d_ave_turn]

        return sum([p*d for p, d in zip(win_probs, d_ave)])
    
    def group_damage_sigma(self, group_name, **kwargs):
        """returns the average final damage for the given group.
        """
        return np.sqrt(self.group_damage_variance(group_name, **kwargs))
    
    def group_damage_variance(self, group_name, **kwargs):
        """returns the variance of the final damage distribution for the given group.
        """
        method = kwargs.get('method', 'exact')
        if method == 'approx':
            return self.group_damage_variance_approx(group_name, **kwargs)
        else:
            return self.group_damage_distribution(group_name, **kwargs).variance()
    
    def group_damage_variance_approx(self, group_name, **kwargs):
        """returns the variance of the final damage distribution for the given group.
        """
        clip = kwargs.get('clip', False)

        group_damage_mean = self.group_damage_mean_approx(group_name, **kwargs)
        cdf = self.group_damage_cdf_approx(group_name)
        opponent = self.groups[group_name]['opponent']
        opponent_hit_points = self.groups[opponent]['hit points']
        win_probs = np.array(self.encounter_win_pdf(**kwargs))

        d_var = []
        damage_mean = 0
        damage_var = 0
        for i in range(len(self.turns)):
            t = self.turns[i]

            if t['group'] == group_name:
                c = self.get_combatant(t['name'])
                damage_mean += c.dpr(t['round']).mean()
                damage_var += c.dpr(t['round']).variance()

                if clip:
                    d_ave_turn = opponent_hit_points
                    d_var_turn = 0
                else:
                    d_ave_turn = damage_mean
                    d_var_turn = damage_var
            else:
                d_var_turn = 0
                d_ave_turn = 0
                if (damage_mean > 0) and (cdf[i] < 1):

                    g = gaussian(damage_mean, np.sqrt(damage_var), opponent_hit_points - 0.5)/(1 - cdf[i])
                    d_ave_turn = damage_mean - damage_var*g
                    d2_ave_turn = damage_mean**2 + damage_var*(1 - (opponent_hit_points - 0.5 + damage_mean)*g)
                    d_var_turn = d2_ave_turn - d_ave_turn**2
                    
                    d_var_turn = damage_var + damage_var*(damage_mean - (opponent_hit_points - 0.5))*g - (damage_var*g)**2

            
            if d_var_turn < 0:
                # not sure why this happens, but this seems to work OK as a fix ...
                """print(f'{i}:')
                print(f' - {d_var_turn}')
                print(f'   {damage_mean}')
                print(f'   {damage_var}')
                print(f'   {g}')
                print(f'   {(damage_mean - (opponent_hit_points - 0.5))}')
                print(f'   {damage_var*g}')"""

                d_var_turn = 0
            
            d_var += [d_var_turn + (group_damage_mean - d_ave_turn)**2]
            #d_var += [(group_damage_mean - d_ave_turn)**2]

        return sum([p*d for p, d in zip(win_probs, d_var)])

    def group_overdamage(self, group_name, turn, **kwargs):
        """Returns the overdamage distribution for the given group at the end of rounds of combat.
        """
        
        damage = self.group_damage(group_name, turn-1)

        opponent = self.groups[group_name]['opponent']
        opponent_hit_points = self.groups[opponent]['hit points']
        damage, _ = split_overdamage(damage, opponent_hit_points)

        t =  self.turns[turn]
        if t['name'] and t['group'] == group_name:
            damage += self.get_combatant(t['name']).dpr(t['round'])

        damage, over_damage = split_overdamage(damage, opponent_hit_points)
        
        return damage, over_damage
    
    def group_win_cdf(self, group_name, **kwargs):
        """Returns the cumulative probability of the given group winning the
        encounter during each turn or before."""
        pdf = self.group_win_pdf(group_name, **kwargs)
        return list(np.cumsum(pdf))
    
    def group_win_pdf(self, group_name, **kwargs):
        """Returns the probability of the given group winning the
        encounter during each turn."""
        g_pdf = self.group_damage_pdf(group_name, **kwargs)
        opponent = self.groups[group_name]['opponent']
        o_cdf = self.group_damage_cdf(opponent, **kwargs)
        return [p*(1 - c) for p, c in zip(g_pdf, o_cdf)]
    
    def group_win_pct(self, group_name, **kwargs):
        """Returns the probability of the given group winning the encounter.
        """
        return max(self.group_win_cdf(group_name, **kwargs))
    
    def plot_probability_diagram(self, fig):
        groups = [g for g in self.groups]
        turns = self.turns
        cdf_0 = self.group_damage_cdf(groups[0])
        pdf_0 = self.group_damage_pdf(groups[0])
        cdf_1 = self.group_damage_cdf(groups[1])
        pdf_1 = self.group_damage_pdf(groups[1])
        for t, p0, c0, p1, c1 in zip(turns, pdf_0, cdf_0, pdf_1, cdf_1):
            if p0 + p1 == 0: continue
            if c0+c1 >= 2: continue
            group = t['group']
            round = t['round']
            turn = t['turn'] - (round - 1)*len(self.combatants)
            if group == groups[0]:
                fig.add_shape(
                    type="rect",
                    x0=c0-p0, x1=c0,
                    y0=c1, y1=1,
                    line=dict(color='rgba(250,250,250,1)', width=1),
                    fillcolor='red',
                    opacity=0.3,
                )
                fig.add_trace(go.Scatter(
                    x=[(c0-p0 + c0)/2],
                    y=[(c1 + 1)/2],
                    text=[f"{round:.0f}.{turn:.0f}"],
                    mode='text',
                    showlegend=False,
                    hovertemplate=
                        f'{group}<br>'+
                        f'Round {round:.0f}<br>'+
                        f'Turn {turn:.0f}<br>'+
                        f'Win PDF {p0*(1 - c1):.3%}<extra></extra>'
                ))
            elif group == groups[1]:
                fig.add_shape(
                    type="rect",
                    x0=c0, x1=1,
                    y0=c1-p1, y1=c1,
                    line=dict(color='rgba(250,250,250,1)', width=1),
                    fillcolor='blue',
                    opacity=0.3,
                )
                fig.add_trace(go.Scatter(
                    x=[(c0 + 1)/2],
                    y=[(c1-p1 + c1)/2],
                    text=[f"{round:.0f}.{turn:.0f}"],
                    mode='text',
                    showlegend=False,
                    hovertemplate=
                        f'{group}<br>'+
                        f'Round {round:.0f}<br>'+
                        f'Turn {turn:.0f}<br>'+
                        f'Win PDF {p1*(1 - c0):.3%}<extra></extra>'
                ))

def baseline_pc(level):
    return {
        'level': level,
        'hit points': 1 + 7*level,
        'attack bonus': np.round( 4.6 + level/3, 0),
        'armor class':  np.round(14.7 + level/6, 0),
        'save bonus':   np.round( 1.5 + level/5, 0),
    }