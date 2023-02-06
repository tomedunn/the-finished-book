import copy
import numpy as np
import diceEq as de
import estats5e as es5
import itertools as itt

# utility
def remove_empty_data( obj ):
    if type(obj) == list:
        for i in range(len(obj)):
            obj[i] = remove_empty_data(obj[i])
        obj = [l for l in obj if l]
    elif type(obj) == dict:
        for k in obj:
            obj[k] = remove_empty_data(obj[k])
        obj = {k: v for k, v in obj.items() if v}
    return obj

# resources
def resourcesUsed(actions=None, rounds=None, resources=None):
    """Returns dictionary of resources and the number of times they're used.
    actions - dictionary of actions.
    rounds - list of rounds to be looped through and counted.
    resources - dictionary of available resources.
    """
    if rounds:
        if not resources: 
            resources = {}
        for round in rounds:
            resources = resourcesUsed(actions=round['actions'], resources=resources)

    if actions:
        if not resources: 
            resources = {}
        for a in actions:
            if actions[a].get('resources', None):
                for r in actions[a]['resources']:
                    if r in resources:
                        resources[r] += -actions[a]['resources'][r]
                    else:
                        resources[r]  = -actions[a]['resources'][r]
    
    if resources == {}:
        return None
    else:
        return resources

def initResources(pc):
    """Returns dictionary with resources and their remaining uses.
    pc - dictionary with player character actions, bonus actions, and reactions.
    """
    resources = {}
    for r in pc['resources']:
        resources[r] = pc['resources'][r]['uses']
    
    return resources

def refreshResources(pc, event, resIn):
    """Returns dictionary with resources and their remaining uses.
    pc - dictionary with player character actions, bonus actions, and reactions.
    event - string trigger for refreshing resources.
    resIn - dictionary of remaining resources.
    """
    resOut = resIn.copy()
    for r in resOut:
        if pc['resources'][r]['recharge'] == event:
            resOut[r] = pc['resources'][r]['uses']
    return resOut

def sufficientResources(resources, used):
    """Returns true if resources used doesn't exceed resources for each resource.
    resources - dictionary of available resources.
    used - dictionary of resources used.
    """
    if used:
        resourcesRemaining = remainingResources(resources, used)
        for r in resourcesRemaining:
            if resourcesRemaining[r] < 0:
                return False
    return True

def remainingResources(resources, used):
    """Returns remaining uses for each resource.
    resources - dictionary of available resources.
    used - dictionary of resources used.
    """
    resourcesRemaining = resources.copy()
    if used:
        for r in used:
            resourcesRemaining[r] -= used[r]
    return resourcesRemaining

def action_uses_remaining(action, resources=None):
    """Returns number of times action can be used
    action - dictionary describing action.
    resources - dictionary of available resources.
    """

    if not action.get('resources', None):
        return np.inf

    if not resources:
        return 0
    
    n_uses = np.inf
    for r in action['resources']:
        if r in resources:
            r_uses = np.floor(resources[r] / -action['resources'][r])
            n_uses = min(n_uses, r_uses)
        else:
            n_uses = 0
            break

    return n_uses

def round_uses_remaining(round, resources=None):
    """Returns number of times action can be used
    round - dictionary of round properties
    resources - dictionary of available resources.
    """

    if not round.get('resources used', None):
        return np.inf

    if not resources:
        return 0
    
    n_uses = np.inf
    for r in round['resources used']:
        if r in resources:
            r_uses = np.floor(resources[r] / round['resources used'][r])
            n_uses = min(n_uses, r_uses)
        else:
            n_uses = 0
            break

    return n_uses

# rounds
def applyEffect(round, effect=None):
    """Returns updated combat stats.
    round - list of rounds.
    effect - dictionary with effect properties.
    """
    if not effect:
        return round
    
    if effect.get('armor class bonus', None):
        round['armor class'] += effect['armor class bonus']

    if effect.get('hit points multiplier', None):
        round['hit points multiplier'] *= effect['hit points multiplier']

    if effect.get('attack bonus bonus', None):
        for i in range(len(round['attack bonus'])):
            round['attack bonus'][i] += effect['attack bonus bonus']

    if effect.get('healing', None):
        round['healing mean'].append(de.rollAverage(effect['healing']))
        round['healing var'].append(np.power(de.rollSigma(effect['healing']), 2))

    if effect.get('damage', None):
        round['damage mean'].append(de.rollAverage(effect['damage']))
        round['damage var'].append(np.power(de.rollSigma(effect['damage']), 2))
        round['attack bonus'].append(effect['attack bonus'])

    if effect.get('actions', None):
        for a in effect['actions']:
            eAct = effect['actions'][a]
            if a in round['actions']:
                rAct = round['actions'][a]
                if 'damage' in eAct:
                    for atk in rAct['attacks']:
                        round['damage mean'].append(de.rollAverage(eAct['damage']))
                        round['damage var'].append(np.power(de.rollSigma(eAct['damage']), 2))
                        round['attack bonus'].append(atk['attack bonus'])
    
    return round

def applyAction(round, action):
    """Returns round updated with the given action.
    round - dictionary of round properties
    action - dictionary of action properties.
    """
    if action.get('armor class bonus', None):
        round['armor class'] += action['armor class bonus']
    
    if action.get('hit points multiplier', None):
        round['hit points multiplier'] *= action['hit points multiplier']

    if action.get('healing', None):
        round['healing mean'].append(de.rollAverage(action['healing']))
        round['healing var'].append(np.power(de.rollSigma(action['healing']), 2))

    if action.get('attacks', None):
        for atk in action['attacks']:
            round['damage mean'].append(de.rollAverage(atk['damage']))
            round['damage var'].append(np.power(de.rollSigma(atk['damage']), 2))
            round['attack bonus'].append(atk['attack bonus'])
    
    return round

def createRound(pc, resources=None, actions=None, effects=None):
    """Returns a round built from the given actions.
    pc - Player character object used to create combat stats.
    resources - dictionary of available resources.
    actions - dictionary of actions and their properties.
    effects - dictionary of effects and their properties.
    """
    round = {
        'healing mean': [],
        'healing var': [],
        'hit points multiplier': pc['hit points multiplier'],
        'armor class': pc['armor class'],
        'damage mean': [],
        'damage var': [],
        'attack bonus': [],
        'actions': actions,
        'effects': effects,
        'resources used': None
    }

    if actions:
        for a in actions:
            round = applyAction(round, actions[a])

    if effects:
        for e in effects:
            round = applyEffect(round, effects[e])
    
    round['resources used'] = resourcesUsed(actions=round['actions'])
    
    if not roundRequirementsMet(round):
        return None
    
    if resources:
        if not sufficientResources(resources, round['resources used']):
            return None

    return copy.deepcopy(round)

def roundRequirementsMet(round):
    """Returns True if the requirements for each action in the round are met.
    round - dictionary of round properties
    """
    actions = round['actions']
    for a in actions:
        action = actions[a]
        if 'requires' in action:
            requirements = action['requires']
            if 'action' in requirements:
                requirementFound = False
                requiredAction = requirements['action'] if type(requirements['action']) == list else [requirements['action']]
                for ra in requiredAction:
                    if ra in actions:
                        requirementFound = True
                if not requirementFound:
                    return False

    return True

# round options
def createRoundOptions(pc, resources, actsLimit=None, bactsLimit=None, ractsLimit=None, **kwargs):
    """Returns list of possible round options. Each a combination of an action, bonus action, and reaction.
    pc - dictionary with player character actions, bonus actions, and reactions.
    resources - dictionary of available resources.
    actsLimit - dictionary of limits to be applied to actions.
    bactsLimit - dictionary of limits to be applied to bonus actions.
    ractsLimit - dictionary of limits to be applied to reactions.
    """
    debugging = kwargs.get('debugging', False)
    # limit actions
    acts = limitActions(pc['actions'], resources=resources, actsLimit=actsLimit, **kwargs)
    bcts = limitActions(pc['bonus actions'], resources=resources, actsLimit=bactsLimit, **kwargs)
    rcts = limitActions(pc['reactions'], resources=resources, actsLimit=ractsLimit, **kwargs)
    if debugging:
        print(pc['actions'])
        print(acts)
        print('\n')
        print(pc['bonus actions'])
        print(bcts)
        print('\n')
        print(pc['reactions'])
        print(rcts)
        print('\n\n')

    # construct rounds
    rounds = []
    for act in acts:
        for bct in bcts:
            for rct in rcts:
                round = createRound(pc, resources, actions={
                    act: acts[act],
                    bct: bcts[bct],
                    rct: rcts[rct]})
                if round:
                    rounds.append(round)
    return rounds

def limitActions(actions, resources=None, actsLimit=None, **kwargs):
    """Returns a list of actions limited to only the top performers with resources remaining.
    actions - dictionary of actions.
    resources - dictionary of available resources.
    actsLimit - dictionary of limits to be applied to acts.
    """
    debugging = kwargs.get('debugging', False)
    method = kwargs.get('effective_method', 'linear')
    limActs = copy.deepcopy(actions)
    if debugging: print('incoming actions:\n', limActs)
    if resources:
        actNames = []
        for a in limActs:
            if not sufficientResources(resources, resourcesUsed(actions={a: limActs[a]})):
                actNames.append(a)
            #if limActs[a]['resources']:
            #    res = limActs[a]['resource']
            #    if limActs[a]['uses']['amount'] > resources[res]:
            #        actNames.append(a)
        for a in actNames:
            if debugging: print(f'removing {a} for insufficient resources.')
            del limActs[a]
    
    if actsLimit:
        if 'top eDPR' in actsLimit:
            nMax = actsLimit['top eDPR']
            eDPRs = []
            actNames = []
            nUses = []
            for a in limActs:
                if limActs[a]['attacks']:
                    eDPR = np.array([es5.effDPR(de.rollAverage(atk['damage']), atk['attack bonus'], method=method) for atk in limActs[a]['attacks']]).sum()
                    eDPRs.append(eDPR)
                    actNames.append(a)
                    nUses.append(action_uses_remaining(limActs[a], resources=resources))
            
            ind = np.argsort(-np.array(eDPRs))
            rUses = 0
            for i in ind:
                if rUses >= nMax:
                    if not 'requires' in limActs[actNames[i]]:
                        if debugging: print(f'removing {actNames[i]} for low eDPR.')
                        del limActs[actNames[i]]
                else:
                    rUses += nUses[i]
            """
            for i in ind[nMax-1:]:
                if not 'requires' in limActs[actNames[i]]:
                    if debugging: print(f'removing {actNames[i]} for low eDPR.')
                    del limActs[actNames[i]]
            """
        
        if 'top healing' in actsLimit:
            nMax = actsLimit['top healing']
            heals = []
            actNames = []
            nUses = []
            for a in limActs:
                if limActs[a]['healing']:
                    heals.append(de.rollAverage(limActs[a]['healing']))
                    actNames.append(a)
                    nUses.append(action_uses_remaining(limActs[a], resources=resources))

            ind = np.argsort(-np.array(heals))
            rUses = 0
            for i in ind:
                if rUses >= nMax:
                    if not 'requires' in limActs[actNames[i]]:
                        if debugging: print(f'removing {actNames[i]} for low healing.')
                        del limActs[actNames[i]]
                else:
                    rUses += nUses[i]
            """
            for i in ind[nMax-1:]:
                if not 'requires' in limActs[actNames[i]]:
                    if debugging: print(f'removing {actNames[i]} for low healing.')
                    del limActs[actNames[i]]
            """

        if 'pad None' in actsLimit:
            nMax = actsLimit['pad None']
            
            #r_uses = [action_uses_remaining(limActs[a], resources=resources) if a != 'None' else 0 for a in limActs]
            #n_uses = np.sum(r_uses)

            n_uses = 0
            for a in limActs:
                if a == 'None':
                    continue
                if 'effect' in limActs[a]:
                    if limActs[a]['effect']:
                        if limActs[a]['effect']['duration'] > 1:
                            continue
                n_uses += action_uses_remaining(limActs[a], resources=resources)

            if n_uses >= nMax:
                if 'None' in limActs:
                    if debugging: print(f'removing None for being unnecessary.')
                    limActs.pop('None')
            else:
                if 'None' not in limActs:
                    if debugging: print(f'adding None to pad actions.')
                    limActs['None'] = {
                        'attacks': None,
                        'healing': None,
                        'armor class bonus': None,
                        'hit points multiplier': None,
                        'resources': None,
                        'effect': None
                    }
            


            """
            if 'None' in limActs:
                #act = limActs.pop('None')
                nMax = actsLimit['pad None']
                r_uses = [action_uses_remaining(limActs[a], resources=resources) if a != 'None' else 0 for a in limActs]
                n_uses = np.sum(r_uses)
                if n_uses >= nMax:
                    limActs.pop('None')
                    #limActs['None'] = act
            """

            """
            nMax = actsLimit['pad None']
            r_uses = [action_uses_remaining(limActs[a], resources=resources) for a in limActs]
            nUses = np.sum(r_uses)
            print(nMax, ':', nUses, '-', r_uses)
            if nUses < nMax:
                limActs['None'] = {
                    'attacks': None,
                    'healing': None,
                    'armor class bonus': None,
                    'hit points multiplier': None,
                    'resources': None,
                    'effect': None
                }
                r_uses = [action_uses_remaining(limActs[a], resources=resources) for a in limActs]
                nUses = np.sum(r_uses)
                print('new', nMax, ':', nUses, '-', r_uses)
            #elif 'None' in limActs:
            #    del limActs['None']
            """
    if debugging: print('final actions:\n', limActs)
    return limActs

# encounters
def encounterEngine_old(pc, rounds, resources, roundOptions, i=0, **kwargs):
    """Returns highest XP rounds for encounter.
    pc - dictionary with player character actions, bonus actions, and reactions.
    rounds - list of initial rounds for encounter.
    resources - dictionary of available resources.
    roundOptions - list of rounds that can be picked for encounter.
    i - integer round number.
    """
    XPmax = 0
    eSumMax = encounterSummary(pc, rounds, **kwargs)
    for ro in roundOptions:
        rounds[i] = copy.deepcopy(ro)
        rUsed = resourcesUsed(rounds=rounds)
        if sufficientResources(resources, rUsed):
            if i == len(rounds)-1:
                eSum = encounterSummary(pc, rounds, **kwargs)
            else:
                # look for the best rounds following this one in the encounter
                eSum = encounterEngine(pc, rounds, resources, roundOptions, i=i+1, **kwargs)
                rounds = copy.deepcopy(eSum['rounds'])

            tXP = eSum['XP mean']
            if tXP > XPmax:
                XPmax = tXP
                eSumMax = copy.deepcopy(eSum)
            #elif (tXP == XPmax):
            #    if compareResources(eSum['resources used'], eSumMax['resources used']) == -1: # eSum uses less resources than eSumMax
            #        XPmax = tXP
            #        eSumMax = eSum.copy()
    
    eSumMax['round options'] = roundOptions
    return eSumMax

def encounterEngine(pc, rounds, resources, roundOptions, i=0, **kwargs):
    """Returns highest XP rounds for encounter.
    pc - dictionary with player character actions, bonus actions, and reactions.
    rounds - list of initial rounds for encounter.
    resources - dictionary of available resources.
    roundOptions - list of rounds that can be picked for encounter.
    """
    # order options so those with effects are listed first
    round_options = []
    for ro in roundOptions:
        if any([act.get('effect', None) != None for act in ro['actions'].values()]):
            round_options.append(ro)
        
    for ro in roundOptions:
        if all([act.get('effect', None) == None for act in ro['actions'].values()]):
            round_options.append(ro)

    # loop through each combination of rounds to find the highest encounter XP
    xp_max = 0
    enc_max = []
    rUsed_max = {}
    for enc in itt.combinations_with_replacement(range(len(round_options)), len(rounds)):
        rounds = [round_options[i] for i in list(enc)]
        rUsed = resourcesUsed(rounds=rounds)
        if sufficientResources(resources, rUsed):
            eSum = encounterSummary(pc, rounds, **kwargs)
            if eSum['XP mean'] > xp_max:
                xp_max = eSum['XP mean']
                enc_max = list(enc)
                rUsed_max = rUsed.copy() if rUsed else {}
            elif eSum['XP mean'] == xp_max:
                # pick one that used fewer resources:
                if np.sum(list(rUsed.values())) < np.sum(list(rUsed_max.values())):
                    xp_max = eSum['XP mean']
                    enc_max = list(enc)
                    rUsed_max = rUsed.copy() if rUsed else {}

    rounds = [round_options[i] for i in enc_max]
    eSum = encounterSummary(pc, rounds, **kwargs)
    eSum['round options'] = round_options
    return eSum

"""
Should add a way for determining when a simpler encounter engine can be used.
If each resource that can be used can only be used by one action, then we can
pick the best actions independently of each other type of action.

Actions that have no immediate payoff and only produce an effect can be ignored
until that effect ends.

If all rounds can be filled with actions, then a None action isn't needed.
"""

def encounterSummary(pc, rounds, **kwargs):
    """Returns summary object of combat actions.
    pc - dictionary with player character actions, bonus actions, and reactions.
    rounds - list of encounter rounds.
    """
    method = kwargs.get('effective_method', 'linear')
    # manage effects
    rnds = copy.deepcopy(rounds)
    effects = {}
    for i in range(len(rnds)):
        actions = rnds[i]['actions']
        effects = updateEffects(effects, actions)
        rnds[i] = createRound(pc, actions=actions, effects=effects)

    # calculate stats
    hpm = de.rollAverage(pc['hit points'])
    hpv = np.power(de.rollSigma(pc['hit points']), 2)
    hlm = 0.0; hlv = 0.0
    hmm = 0.0
    acm = 0.0
    dm  = 0.0; dv  = 0.0
    abm = 0.0
    for r in rnds:
        hlm += np.array(r['healing mean']).sum()
        hlv += np.array(r['healing var']).sum()
        hmm += r['hit points multiplier']
        acm += r['armor class']
        dm  += np.array(r['damage mean']).sum()
        dv  += np.array(r['damage var']).sum()
        abm += np.dot(np.array(r['attack bonus']), np.array(r['damage mean']))
    
    hmm  = hmm/len(rnds)
    acm  = acm/len(rnds)
    dprm = dm/len(rnds)
    dprv = dv/len(rnds)
    abm  = abm/max(dm, 1.0)

    eHPm  = es5.effHP((hpm + hlm)*hmm, acm, method=method)
    eHPv  = np.power(es5.effHP(np.sqrt(hpv + hlv)*hmm, acm, method=method), 2)
    eDPRm = es5.effDPR(dprm, abm, method=method)
    eDPRv = np.power(es5.effDPR(np.sqrt(dprv), abm, method=method), 2)
    eXPm  = es5.effXP((hpm + hlm)*hmm, acm, dprm, abm, method=method, ctype='PC')
    eXPv  = np.power(es5.effXP((hpm + hlm)*hmm, acm, np.sqrt(dprv), abm, method=method, ctype='PC'), 2) \
          + np.power(es5.effXP(np.sqrt(hpv + hlv)*hmm, acm, dprm, abm, method=method, ctype='PC'), 2) \
          + np.power(es5.effXP(np.sqrt(hpv + hlv)*hmm, acm, np.sqrt(dprv), abm, method=method, ctype='PC'), 2)
    eSum = {
        'type': 'encounter',
        'hit points mean': hpm,
        'hit points var': hpv,
        'healing mean': hlm,
        'healing var': hlv,
        'hit points multiplier': hmm,
        'armor class': acm,
        'effective hit points mean': eHPm,
        'effective hit points var': eHPv,
        'damage per round mean': dprm,
        'damage per round var': dprv,
        'attack bonus': abm,
        'effective damage per round mean': eDPRm,
        'effective damage per round var': eDPRv,
        'XP mean': eXPm,
        'XP var': eXPv,
        'rounds': rnds,
        'resources used': resourcesUsed(rounds=rnds)
    }
    #pprint.pprint(eSum)
    return copy.deepcopy(eSum)

def updateEffects(effects=None, actions=None):
    """Returns effects dictionary.
    actions - dictionary of actions and their properties.
    effects - dictionary of effects and their properties.
    """
    #if not effects:
    #    return None
    
    # Reduce effect durations and remove expired effects
    expired = []
    for e in effects:
        effect = effects[e]
        effect['duration'] = max(effect['duration'] - 1, 0)
        if effect['duration'] < 1:
            expired.append(e)
    for e in expired:
        del effects[e]

    # add new effects
    for a in actions:
        act = actions[a]
        if act['effect']:
            effects[a] = act['effect']
    
    return copy.deepcopy(effects)

# short rests
def shortRestEngine(pc, resources):
    """Returns short rest summary dictionary.
    pc - dictionary with player character actions, bonus actions, and reactions.
    resources - dictionary of available resources.
    """
    resRemaining = resources.copy()
    rnds = []
    # short rest actions
    for a in pc['short rests']:
        act = pc['short rests'][a]
        if act['healing']:
            rnd = createRound(pc, actions={a: act})
            if act['resources']:
                for r in act['resources']:
                    n = int(np.floor(resRemaining[r]/rnd['resources used'][r]))
                    for i in range(n):
                        rnds.append(rnd)
                        resRemaining = remainingResources(resRemaining, rnd['resources used'])
            else:
                rnds.append(rnd)
    
    # other actions that heal and recharge on short rest
    for t in ['actions','bonus actions']:
        for a in pc[t]:
            act = pc[t][a]
            if act['healing'] and act['resources']:
                for r in act['resources']:
                    if pc['resources'][r]['recharge'] == 'short rest':
                        rnd = createRound(pc, actions={a: act})
                        n = int(np.floor(resRemaining[r]/rnd['resources used'][r]))
                        for i in range(n):
                            rnds.append(rnd)
                            resRemaining = remainingResources(resRemaining, rnd['resources used'])
    
    return shortRestSummary(pc, rnds)

def shortRestSummary(pc, rounds):
    """Returns dictionary summary of short rest actions.
    pc - dictionary with player character actions, bonus actions, and reactions.
    rounds - list of short rest "rounds".
    """
    hpm = de.rollAverage(pc['hit points'])
    hpv = np.power(de.rollSigma(pc['hit points']), 2)
    hlm = np.array([r['healing mean'] for r in rounds]).sum()
    hlv = np.array([r['healing var'] for r in rounds]).sum()
    hmm = 0
    acm = 0
    eHPm = 0
    eHPv = 0
    dprm = 0
    dprv = 0
    abm  = 0
    eDPRm = 0
    eDPRv = 0
    eXPm  = 0
    eXPv  = 0
    rSum = {
        'type': 'short rest',
        'hit points mean': hpm,
        'hit points var': hpv,
        'healing mean': hlm,
        'healing var': hlv,
        'hit points multiplier': hmm,
        'armor class': acm,
        'effective hit points mean': eHPm,
        'effective hit points var': eHPv,
        'damage per round mean': dprm,
        'damage per round var': dprv,
        'attack bonus': abm,
        'effective damage per round mean': eDPRm,
        'effective damage per round var': eDPRv,
        'XP mean': eXPm,
        'XP var': eXPv,
        'rounds': rounds,
        'resources used': resourcesUsed(rounds=rounds)
    }
    return copy.deepcopy(rSum)

# long rests
def longRestEngine(pc, resources):
    """Returns long rest summary dictionary.
    pc - dictionary with player character actions, bonus actions, and reactions.
    resources - dictionary of available resources.
    """
    resRemaining = resources.copy()
    rnds = []
    # long rest actions
    for a in pc['long rests']:
        act = pc['long rests'][a]
        if act['healing']:
            rnd = createRound(pc, actions={a: act})
            if act['resources']:
                for r in act['resources']:
                    n = int(np.floor(resRemaining[r]/rnd['resources used'][r]))
                    for i in range(n):
                        rnds.append(rnd)
                        resRemaining = remainingResources(resRemaining, rnd['resources used'])
            else:
                rnds.append(rnd)
    
    # other actions that heal and recharge on long or short rest
    for t in ['actions','bonus actions']:
        for a in pc[t]:
            act = pc[t][a]
            if act['healing'] and act['resources']:
                for r in act['resources']:
                    if (pc['resources'][r]['recharge'] == 'long rest') or (pc['resources'][r]['recharge'] == 'short rest'):
                        rnd = createRound(pc, actions={a: act})
                        n = int(np.floor(resRemaining[r]/rnd['resources used'][r]))
                        for i in range(n):
                            rnds.append(rnd)
                            resRemaining = remainingResources(resRemaining, rnd['resources used'])
    
    return longRestSummary(pc, rnds)

def longRestSummary(pc, rounds):
    """Returns dictionary summary of long rest actions.
    pc - dictionary with player character actions, bonus actions, and reactions.
    rounds - list of short rest "rounds".
    """
    hpm = de.rollAverage(pc['hit points'])
    hpv = np.power(de.rollSigma(pc['hit points']), 2)
    hlm = np.array([r['healing mean'] for r in rounds]).sum()
    hlv = np.array([r['healing var'] for r in rounds]).sum()
    hmm = 0
    acm = 0
    eHPm = 0
    eHPv = 0
    dprm = 0
    dprv = 0
    abm  = 0
    eDPRm = 0
    eDPRv = 0
    eXPm  = 0
    eXPv  = 0
    rSum = {
        'type': 'long rest',
        'hit points mean': hpm,
        'hit points var': hpv,
        'healing mean': hlm,
        'healing var': hlv,
        'hit points multiplier': hmm,
        'armor class': acm,
        'effective hit points mean': eHPm,
        'effective hit points var': eHPv,
        'damage per round mean': dprm,
        'damage per round var': dprv,
        'attack bonus': abm,
        'effective damage per round mean': eDPRm,
        'effective damage per round var': eDPRv,
        'XP mean': eXPm,
        'XP var': eXPv,
        'rounds': rounds,
        'resources used': resourcesUsed(rounds=rounds)
    }
    return copy.deepcopy(rSum)

# adventuring days
def dailyEngine(pc, day, **kwargs):
    """
    pc - dictionary with player character actions, bonus actions, and reactions.
    day - list of encounters and rests.
    """
    resources = initResources(pc)
    resRemaining = resources.copy()
    encounters = []
    rndZero = createRound(pc, resources, actions={
        'None': {
            'attacks': None,
            'healing': None,
            'armor class bonus': None,
            'hit points multiplier': None,
            'resources': None,
            'effect': None
        }})
    for x in day:
        if x['type'] == 'encounter':
            nRounds = x['rounds']
            actsLimit = {
                'top eDPR': 2*nRounds, 
                'top healing': 1 if kwargs.get('combat healing', True) else 0, 
                'pad None': nRounds
            }
            rndOpts = createRoundOptions(pc, resRemaining, 
                actsLimit=actsLimit, 
                bactsLimit={'top eDPR': 2*nRounds, 'pad None': nRounds},
                ractsLimit={'pad None': nRounds},
                **kwargs)
            
            #rounds = [rndOpts[0]]*nRounds
            rounds = [rndZero]*nRounds
            eSum = encounterEngine(pc, rounds, resRemaining, rndOpts, i=0, **kwargs)
            encounters += [eSum]
            resRemaining = remainingResources(resRemaining, eSum['resources used'])
        elif x['type'] == 'short rest':
            sSum = shortRestEngine(pc, resRemaining)
            encounters += [sSum]
            resRemaining = remainingResources(resRemaining, sSum['resources used'])
            resRemaining = refreshResources(pc, 'short rest', resRemaining)
        elif x['type'] == 'long rest':
            lSum = longRestEngine(pc, resRemaining)
            encounters += [lSum]
            resRemaining = remainingResources(resRemaining, lSum['resources used'])
            resRemaining = refreshResources(pc, 'short rest', resRemaining)
    
    dSum = dailySummary(pc, encounters, **kwargs)
    
    if kwargs.get('remove empty data', False):
        dSum = remove_empty_data(dSum)
    
    if kwargs.get('simplify summary', False):
        dSum = simplify_summary(dSum)

    return dSum

def dailySummary(pc, encounters, **kwargs):
    """Returns summary object of daily encounters.
    pc - dictionary with player character actions, bonus actions, and reactions.
    encounters - list of encounters.
    """
    method = kwargs.get('effective_method', 'linear')
    hpm = de.rollAverage(pc['hit points'])
    hpv = np.power(de.rollSigma(pc['hit points']), 2)
    hlm = 0; hlv = 0
    hmm = 0
    acm = 0
    dprm = 0; dprv = 0
    abm = 0
    eXPm = 0
    eXPv = 0
    cRnds = 0
    rounds = []
    for e in encounters:
        rounds += e['rounds']
        hlm += e['healing mean']
        hlv += e['healing var']
        if e['type'] == 'encounter':
            cRnds += len(e['rounds'])
            hmm  += e['hit points multiplier']*len(e['rounds'])
            acm  += e['armor class']*len(e['rounds'])
            dprm += e['damage per round mean']*len(e['rounds'])
            dprv += e['damage per round var']*len(e['rounds'])
            abm  += e['attack bonus']*len(e['rounds'])
            eXPm += e['XP mean']*len(e['rounds'])
            eXPv += e['XP var']*len(e['rounds'])
    hmm  /= cRnds
    acm  /= cRnds
    dprm /= cRnds
    dprv /= cRnds
    abm  /= cRnds
    eXPm /= cRnds
    eXPv /= cRnds
    
    eHPm = es5.effHP((hpm + hlm)*hmm, acm, method=method)
    eHPv = np.power(es5.effHP(np.sqrt(hpv + hlv)*hmm, acm, method=method), 2)
    eDPRm = es5.effDPR(dprm, abm, method=method)
    eDPRv = np.power(es5.effDPR(np.sqrt(dprv), abm, method=method), 2)
    dXPm  = es5.effXP((hpm + hlm)*hmm, acm, dprm, abm, method=method, ctype='PC')
    dXPv  = np.power(es5.effXP((hpm + hlm)*hmm, acm, np.sqrt(dprv), abm, method=method, ctype='PC'), 2) \
          + np.power(es5.effXP(np.sqrt(hpv + hlv)*hmm, acm, dprm, abm, method=method, ctype='PC'), 2) \
          + np.power(es5.effXP(np.sqrt(hpv + hlv)*hmm, acm, np.sqrt(dprv), abm, method=method, ctype='PC'), 2)
    eSum = {
        'type': 'day',
        'hit points mean': hpm,
        'hit points var': hpv,
        'healing mean': hlm,
        'healing var': hlv,
        'hit points multiplier': hmm,
        'armor class': acm,
        'effective hit points mean': eHPm,
        'effective hit points var': eHPv,
        'damage per round mean': dprm,
        'damage per round var': dprv,
        'attack bonus': abm,
        'effective damage per round mean': eDPRm,
        'effective damage per round var': eDPRv,
        'XP mean': dXPm,
        'XP var': dXPv,
        'encounter XP mean': eXPm,
        'encounter XP var': eXPv,
        'encounters': encounters,
        'resources used': resourcesUsed(rounds=rounds)
    }
    return copy.deepcopy(eSum)

def simplify_summary( dSum ):
    for enc in dSum['encounters']:
        if 'round options' in enc:
            enc.pop('round options')

        if 'rounds' not in enc:
            continue
        
        for ir in range(len(enc['rounds'])):
            rnd = enc['rounds'][ir]
            new_rnd = {}
            if rnd.get('actions', None):
                new_rnd['actions'] = [a for a in rnd['actions']]
            if rnd.get('effects', None):
                new_rnd['effects'] = [e for e in rnd['effects']]
            if rnd.get('resources used', None):
                new_rnd['resources used'] = rnd['resources used']
            enc['rounds'][ir] = new_rnd

    return dSum