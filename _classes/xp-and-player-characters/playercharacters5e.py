import re
import numpy as np
import diceEq as de

# general
def abilityScores_l2d(abs):
    return {'Strength': abs[0], 'Dexterity': abs[1], 'Constitution': abs[2], 'Intelligence': abs[3], 'Wisdom': abs[4], 'Charisma': abs[5]}

def abilityModifier(score):
    return int(np.floor(score/2) - 5)

def proficiencyBonus(lvl):
    return int(np.floor((lvl - 1)/4) + 2)

def hitPointsEquation(lvl, hitDie, stats):
    return '{:} + {:d}{:} + {:d}'.format(hitDie[1:], lvl-1, hitDie, lvl*abilityModifier(stats['Constitution']))

def hitDieHealingEquation(hitDie, stats):
    return '{:} + {:d}'.format(hitDie, abilityModifier(stats['Constitution']))

def pactMagicSlots(lvl):
    slots = [
        #cantrip 1  2  3  4  5  6  7  8  9
        [np.inf, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [np.inf, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [np.inf, 0, 2, 0, 0, 0, 0, 0, 0, 0],
        [np.inf, 0, 2, 0, 0, 0, 0, 0, 0, 0],
        [np.inf, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [np.inf, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [np.inf, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [np.inf, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [np.inf, 0, 0, 0, 0, 2, 0, 0, 0, 0],
        [np.inf, 0, 0, 0, 0, 2, 0, 0, 0, 0],
        [np.inf, 0, 0, 0, 0, 3, 1, 0, 0, 0],
        [np.inf, 0, 0, 0, 0, 3, 1, 0, 0, 0],
        [np.inf, 0, 0, 0, 0, 3, 1, 1, 0, 0],
        [np.inf, 0, 0, 0, 0, 3, 1, 1, 0, 0],
        [np.inf, 0, 0, 0, 0, 3, 1, 1, 1, 0],
        [np.inf, 0, 0, 0, 0, 3, 1, 1, 1, 0],
        [np.inf, 0, 0, 0, 0, 4, 1, 1, 1, 1],
        [np.inf, 0, 0, 0, 0, 4, 1, 1, 1, 1],
        [np.inf, 0, 0, 0, 0, 4, 1, 1, 1, 1],
        [np.inf, 0, 0, 0, 0, 4, 1, 1, 1, 1]
    ]
    return slots[lvl-1]

def spellSlots(lvl):
    slots = [
        #cantrip 1  2  3  4  5  6  7  8  9
        [np.inf, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [np.inf, 3, 0, 0, 0, 0, 0, 0, 0, 0],
        [np.inf, 4, 2, 0, 0, 0, 0, 0, 0, 0],
        [np.inf, 4, 3, 0, 0, 0, 0, 0, 0, 0],
        [np.inf, 4, 3, 2, 0, 0, 0, 0, 0, 0],
        [np.inf, 4, 3, 3, 0, 0, 0, 0, 0, 0],
        [np.inf, 4, 3, 3, 1, 0, 0, 0, 0, 0],
        [np.inf, 4, 3, 3, 2, 0, 0, 0, 0, 0],
        [np.inf, 4, 3, 3, 3, 1, 0, 0, 0, 0],
        [np.inf, 4, 3, 3, 3, 2, 0, 0, 0, 0],
        [np.inf, 4, 3, 3, 3, 2, 1, 0, 0, 0],
        [np.inf, 4, 3, 3, 3, 2, 1, 0, 0, 0],
        [np.inf, 4, 3, 3, 3, 2, 1, 1, 0, 0],
        [np.inf, 4, 3, 3, 3, 2, 1, 1, 0, 0],
        [np.inf, 4, 3, 3, 3, 2, 1, 1, 1, 0],
        [np.inf, 4, 3, 3, 3, 2, 1, 1, 1, 0],
        [np.inf, 4, 3, 3, 3, 2, 1, 1, 1, 1],
        [np.inf, 4, 3, 3, 3, 2, 1, 1, 1, 1],
        [np.inf, 4, 3, 3, 3, 2, 2, 1, 1, 1],
        [np.inf, 4, 3, 3, 3, 2, 2, 2, 1, 1]
    ]
    return slots[lvl-1]

def spellDamage(lvl):
    if   lvl >= 17:
        ctrpDmg = '8d6'
    elif lvl >= 11:
        ctrpDmg = '6d6'
    elif lvl >=  5:
        ctrpDmg = '4d6'
    else:
        ctrpDmg = '2d6'
    return [ctrpDmg,'3d8','6d6','10d6','9d8','10d10','15d8','14d10','15d10','19d10']

def spellHealing(lvl):
    return ['0','2d10','3d10','5d10','6d10','8d10','10d10','11d10','12d10','15d10']

# actions
def newAction(attacks=None, healing=None, acbonus=None, hpmultiplier=None, resources=None, effect=None, **kwargs):
    action = {
        'attacks': attacks,
        'healing': healing,
        'armor class bonus': acbonus,
        'hit points multiplier': hpmultiplier,
        'resources': resources,
        'effect': effect
    }
    for k in kwargs:
        action[k] = kwargs[k]

    return action

def newEffect(duration=0, damage=None, healing=None, abbonus=None, acbonus=None, hpmultiplier=None, actions=None, **kwargs):
    effect = {
        'duration': duration,
        'damage': damage,
        'healing': healing,
        'armor class bonus': acbonus,
        'attack bonus bonus': abbonus,
        'hit points multiplier': hpmultiplier,
        'actions': actions
    }
    for k in kwargs:
        effect[k] = kwargs[k]

    return effect

def newResource(uses=None, recharge=None, **kwargs):
    resource = {
        'uses': uses,
        'recharge': recharge
    }
    for k in kwargs:
        resource[k] = kwargs[k]

    return resource

def newASI(**kwargs):
    """Returns dict representing either an ASI or a feat.
    kwargs -- dict of keyword arguments.
        feat -- string name of feat
        strength - integer bonus to Strength score
        dexterity - integer bonus to Dexterity score
        constitution - integer bonus to Constitution score
        intelligence - integer bonus to Intelligence score
        wisdom - integer bonus to Wisdom score
        charisma - integer bonus to Charisma score
    """
    if 'feat' in kwargs:
        asi = {
            'type': 'feat',
            'feat': kwargs.get('feat', None),
        }
    else:
        asi = {
            'type': 'ability score improvement',
            'Strength': kwargs.get('strength', 0), 
            'Dexterity': kwargs.get('dexterity', 0), 
            'Constitution': kwargs.get('constitution', 0), 
            'Intelligence': kwargs.get('intelligence', 0), 
            'Wisdom': kwargs.get('wisdom', 0),  
            'Charisma': kwargs.get('charisma', 0)
        }
    
    return asi

def applyASI(stats, asi):
    """Returns dict of updated stats
    stats -- dict of ability scores.
    asi -- dict of ability score improvements.
    """
    if asi['type'] == 'ability score improvement':
        stats['Strength'] += asi['Strength']
        stats['Dexterity'] += asi['Dexterity']
        stats['Constitution'] += asi['Constitution']
        stats['Intelligence'] += asi['Intelligence']
        stats['Wisdom'] += asi['Wisdom']
        stats['Charisma'] += asi['Charisma']
    return stats

# equipment
def armor(name, stats):
    m = re.match(r'(\w+(?:\s+\w+)?)\s*(\+\d)?', name)
    acB = int(m.group(2)) if m.group(2) else 0
    dexMod = abilityModifier(stats['Dexterity'])
    arms = {
        'none':            {'armor class': 10 + dexMod },
        # light armor
        'padded':          {'armor class': 11 + dexMod + acB},
        'leather':         {'armor class': 11 + dexMod + acB},
        'studded leather': {'armor class': 12 + dexMod + acB},
        # medium armor
        'hide':            {'armor class': 12 + min(dexMod, 2) + acB},
        'chain shirt':     {'armor class': 13 + min(dexMod, 2) + acB},
        'scale mail':      {'armor class': 14 + min(dexMod, 2) + acB},
        'breastplate':     {'armor class': 14 + min(dexMod, 2) + acB},
        'half plate':      {'armor class': 15 + min(dexMod, 2) + acB},
        # heavy armor
        'ring mail':       {'armor class': 14 + acB},
        'chain mail':      {'armor class': 16 + acB},
        'splint':          {'armor class': 17 + acB},
        'plate':           {'armor class': 18 + acB}
    }
    return arms[m.group(1)]

def weapon(name, stats, lvl):
    pb = proficiencyBonus(lvl)
    strMod = abilityModifier(stats['Strength'])
    dexMod = abilityModifier(stats['Dexterity'])
    finMod = max(strMod, dexMod)
    arms = {
        'none':         {'attack bonus': strMod + pb, 'damage': '{:d}'.format(max(strMod, 0))},
        # melee weapons (simple)
        'club':         {'attack bonus': strMod + pb, 'damage': '1d4 + {:d}'.format(strMod)},
        'dagger':       {'attack bonus': finMod + pb, 'damage': '1d4 + {:d}'.format(finMod)},
        'greatclub':    {'attack bonus': strMod + pb, 'damage': '1d8 + {:d}'.format(strMod)},
        'handaxe':      {'attack bonus': strMod + pb, 'damage': '1d6 + {:d}'.format(strMod)},
        'javalin':      {'attack bonus': strMod + pb, 'damage': '1d6 + {:d}'.format(strMod)},
        'light hammer': {'attack bonus': strMod + pb, 'damage': '1d4 + {:d}'.format(strMod)},
        'mace':         {'attack bonus': strMod + pb, 'damage': '1d6 + {:d}'.format(strMod)},
        'quarterstaff': {'attack bonus': strMod + pb, 'damage': '1d6 + {:d}'.format(strMod)},
        'sickle':       {'attack bonus': strMod + pb, 'damage': '1d4 + {:d}'.format(strMod)},
        'spear':        {'attack bonus': strMod + pb, 'damage': '1d6 + {:d}'.format(strMod)},
        # melee weapons (martial)
        'battleaxe':    {'attack bonus': strMod + pb, 'damage': '1d8  + {:d}'.format(strMod)},
        'flail':        {'attack bonus': strMod + pb, 'damage': '1d8  + {:d}'.format(strMod)},
        'glaive':       {'attack bonus': strMod + pb, 'damage': '1d10 + {:d}'.format(strMod)},
        'greataxe':     {'attack bonus': strMod + pb, 'damage': '1d12 + {:d}'.format(strMod)},
        'greatsword':   {'attack bonus': strMod + pb, 'damage': '2d6  + {:d}'.format(strMod)},
        'halberd':      {'attack bonus': strMod + pb, 'damage': '1d10 + {:d}'.format(strMod)},
        'lance':        {'attack bonus': strMod + pb, 'damage': '1d12 + {:d}'.format(strMod)},
        'longsword':    {'attack bonus': strMod + pb, 'damage': '1d8  + {:d}'.format(strMod)},
        'maul':         {'attack bonus': strMod + pb, 'damage': '2d6  + {:d}'.format(strMod)},
        'morningstar':  {'attack bonus': strMod + pb, 'damage': '1d8  + {:d}'.format(strMod)},
        'pike':         {'attack bonus': strMod + pb, 'damage': '1d10 + {:d}'.format(strMod)},
        'rapier':       {'attack bonus': finMod + pb, 'damage': '1d8  + {:d}'.format(finMod)},
        'scimitar':     {'attack bonus': finMod + pb, 'damage': '1d6  + {:d}'.format(finMod)},
        'shortsword':   {'attack bonus': finMod + pb, 'damage': '1d6  + {:d}'.format(finMod)},
        'trident':      {'attack bonus': strMod + pb, 'damage': '1d6  + {:d}'.format(strMod)},
        'war pick':     {'attack bonus': strMod + pb, 'damage': '1d8  + {:d}'.format(strMod)},
        'warhammer':    {'attack bonus': strMod + pb, 'damage': '1d8  + {:d}'.format(strMod)},
        'whip':         {'attack bonus': finMod + pb, 'damage': '1d4  + {:d}'.format(finMod)},
        # ranged weapons (simple)
        'light crossbow': {'attack bonus': dexMod + pb, 'damage': '1d8 + {:d}'.format(dexMod)},
        'dart':           {'attack bonus': dexMod + pb, 'damage': '1d4 + {:d}'.format(dexMod)},
        'shortbow':       {'attack bonus': dexMod + pb, 'damage': '1d6 + {:d}'.format(dexMod)},
        'sling':          {'attack bonus': dexMod + pb, 'damage': '1d4 + {:d}'.format(dexMod)},
        # ranged weapons (martial)
        'blowgun':        {'attack bonus': dexMod + pb, 'damage': '1    + {:d}'.format(dexMod)},
        'hand crossbow':  {'attack bonus': dexMod + pb, 'damage': '1d6  + {:d}'.format(dexMod)},
        'heavy crossbow': {'attack bonus': dexMod + pb, 'damage': '1d10 + {:d}'.format(dexMod)},
        'longbow':        {'attack bonus': dexMod + pb, 'damage': '1d8  + {:d}'.format(dexMod)}
    }

    # select weapon
    m = re.match(r'(\w+(?:\s+\w+)?)\s*([\+\-].+)?', name)
    wpn = arms[m.group(1)]

    # apply weapon damage and attack bonuses
    if m.group(2):
        mod = re.sub(' ', '', m.group(2))
        wpn['damage'] += mod
        m = re.search(r'([\-\+]?(?<!d)\d+(?!d))', mod)
        if m:
            wpn['attack bonus'] += int(m.group(0))
    
    return wpn

# class specific
def monkWeapon(name, stats, lvl):
    pb = proficiencyBonus(lvl)
    strMod = abilityModifier(stats['Strength'])
    dexMod = abilityModifier(stats['Dexterity'])
    finMod = max(strMod, dexMod)
    arms = {
        'none':         {'attack bonus': finMod + pb, 'damage': '1d4 + {:d}'.format(max(finMod, 0))},
        # melee weapons (simple)
        'club':         {'attack bonus': finMod + pb, 'damage': '1d4 + {:d}'.format(finMod)},
        'dagger':       {'attack bonus': finMod + pb, 'damage': '1d4 + {:d}'.format(finMod)},
        'greatclub':    {'attack bonus': finMod + pb, 'damage': '1d8 + {:d}'.format(finMod)},
        'handaxe':      {'attack bonus': finMod + pb, 'damage': '1d6 + {:d}'.format(finMod)},
        'javalin':      {'attack bonus': finMod + pb, 'damage': '1d6 + {:d}'.format(finMod)},
        'light hammer': {'attack bonus': finMod + pb, 'damage': '1d4 + {:d}'.format(finMod)},
        'mace':         {'attack bonus': finMod + pb, 'damage': '1d6 + {:d}'.format(finMod)},
        'quarterstaff': {'attack bonus': finMod + pb, 'damage': '1d6 + {:d}'.format(finMod)},
        'sickle':       {'attack bonus': finMod + pb, 'damage': '1d4 + {:d}'.format(finMod)},
        'spear':        {'attack bonus': finMod + pb, 'damage': '1d6 + {:d}'.format(finMod)},
        # melee weapons (martial)
        'battleaxe':    {'attack bonus': finMod + pb, 'damage': '1d8 + {:d}'.format(finMod)},
        'flail':        {'attack bonus': finMod + pb, 'damage': '1d8 + {:d}'.format(finMod)},
        'longsword':    {'attack bonus': finMod + pb, 'damage': '1d8 + {:d}'.format(finMod)},
        'morningstar':  {'attack bonus': finMod + pb, 'damage': '1d8 + {:d}'.format(finMod)},
        'rapier':       {'attack bonus': finMod + pb, 'damage': '1d8 + {:d}'.format(finMod)},
        'scimitar':     {'attack bonus': finMod + pb, 'damage': '1d6 + {:d}'.format(finMod)},
        'shortsword':   {'attack bonus': finMod + pb, 'damage': '1d6 + {:d}'.format(finMod)},
        'trident':      {'attack bonus': finMod + pb, 'damage': '1d6 + {:d}'.format(finMod)},
        'war pick':     {'attack bonus': finMod + pb, 'damage': '1d8 + {:d}'.format(finMod)},
        'warhammer':    {'attack bonus': finMod + pb, 'damage': '1d8 + {:d}'.format(finMod)},
        'whip':         {'attack bonus': finMod + pb, 'damage': '1d4 + {:d}'.format(finMod)},
        # ranged weapons (simple)
        'light crossbow': {'attack bonus': dexMod + pb, 'damage': '1d8 + {:d}'.format(dexMod)},
        'dart':           {'attack bonus': dexMod + pb, 'damage': '1d4 + {:d}'.format(dexMod)},
        'shortbow':       {'attack bonus': dexMod + pb, 'damage': '1d6 + {:d}'.format(dexMod)},
        'sling':          {'attack bonus': dexMod + pb, 'damage': '1d4 + {:d}'.format(dexMod)},
        # ranged weapons (martial)
        'blowgun':        {'attack bonus': dexMod + pb, 'damage': '1d4 + {:d}'.format(dexMod)},
        'hand crossbow':  {'attack bonus': dexMod + pb, 'damage': '1d6 + {:d}'.format(dexMod)}
    }

    # select weapon
    m = re.match(r'(\w+(?:\s+\w+)?)\s*([\+\-].+)?', name)
    wpn = arms[m.group(1)]
    
    # apply monk weapon damage rules
    if lvl >= 17:
        wpn['damage'] = re.sub(r'(d[468])', 'd10', wpn['damage'])
    elif lvl >= 11:
        wpn['damage'] = re.sub(r'(d[46])', 'd8', wpn['damage'])
    elif lvl >= 5:
        wpn['damage'] = re.sub(r'(d4)', 'd6', wpn['damage'])

    # apply weapon damage and attack bonuses
    if m.group(2):
        mod = re.sub(' ', '', m.group(2))
        wpn['damage'] += mod
        m = re.search(r'([\-\+]?(?<!d)\d+(?!d))', mod)
        if m:
            wpn['attack bonus'] += int(m.group(0))
        
    return wpn

def sorcererFlexibleCasting(lvl, spSlots):
    """Returns spell slots adjusted for flexible casting
    lvl - PC level
    spSlots - list of normal spell slots
    spDmg - list of spell damage
    """
    pts = lvl
    costs = [0,2,3,5,6,7]
    for i in range(5,0,-1):
        n = int(np.floor(pts/costs[i]))
        spSlots[i] += n
        pts -= n*costs[i]
    
    return spSlots
    
def wizardArcaneRecovery(lvl, spSlots, spDmg):
    """Returns spell slots adjusted for arcane recovery
    lvl - PC level
    spSlots - list of normal spell slots
    spDmg - list of spell damage
    """
    pts = int(np.ceil(lvl/2))
    n = min(pts, 5)
    best = 0
    spLvls = [0,0]
    tspDmg = spDmg.copy()
    tspDmg[0] = '0'
    for i in range(n+1):
        for j in range(n+1):
            if i + j <= pts:
                dmg = ' + '.join([tspDmg[i],tspDmg[j]])
                ave = de.rollAverage(dmg)
                if ave > best:
                    best = ave
                    spLvls = [i,j]
    
    spSlots[spLvls[0]] += 1
    spSlots[spLvls[1]] += 1
    return spSlots

# classes
def newPC(pcClass='Barbarian', name='', **kwargs):
    if pcClass == 'Artificer':
        pc = None #artificerPC(name=name, **kwargs)
    elif pcClass == 'Barbarian':
        pc = barbarianPC(name=name, **kwargs)
    elif pcClass == 'Bard':
        pc = bardPC(name=name, **kwargs)
    elif pcClass == 'Cleric':
        pc = clericPC(name=name, **kwargs)
    elif pcClass == 'Druid':
        pc = druidPC(name=name, **kwargs)
    elif pcClass == 'Fighter':
        pc = fighterPC(name=name, **kwargs)
    elif pcClass == 'Monk':
        pc = monkPC(name=name, **kwargs)
    elif pcClass == 'Paladin':
        pc = paladinPC(name=name, **kwargs)
    elif pcClass == 'Ranger':
        pc = rangerPC(name=name, **kwargs)
    elif pcClass == 'Rogue':
        pc = roguePC(name=name, **kwargs)
    elif pcClass == 'Sorcerer':
        pc = sorcererPC(name=name, **kwargs)
    elif pcClass == 'Warlock':
        pc = warlockPC(name=name, **kwargs)
    elif pcClass == 'Wizard':
        pc = wizardPC(name=name, **kwargs)
    
    return pc

def basePC(pcClass, name, lvl, stats, hitdie):
    conMod = abilityModifier(stats['Constitution'])
    pc = {
        'name': name,
        'class': pcClass,
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': hitPointsEquation(lvl, hitdie, stats), 
        'hit points multiplier': 1.0,
        'armor class': 0,
        'actions': {
            'None': newAction()
        },
        'bonus actions': {
            'None': newAction()
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing=hitDieHealingEquation(hitdie, stats), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest')
        }
    }
    return pc

def barbarianPC(name='Barbarian', **kwargs):
    lvl = int(kwargs.get('lvl', 1))

    # stats
    stats = kwargs.get('stats', [16,14,16,8,10,10])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)
    
    asiLvl = [4,8,12,16,19]
    asi = kwargs.get('asi', 2*[newASI(strength=2)] + 2*[newASI(constitution=2)] + [newASI(dexterity=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])

    if lvl >= 20:
        stats['Strength'] += 4
        stats['Constitution'] += 4
    
    dexMod = abilityModifier(stats['Dexterity'])
    conMod = abilityModifier(stats['Constitution'])

    attacks = np.sum(np.array([1,5]) <= lvl)
    rages = 2 + np.sum(np.array([3,6,12,17,20]) <= lvl)
    if lvl >= 20:
        rages = np.inf
    rageBonus = 2 + np.sum(np.array([9,16]) <= lvl)

    # equipment
    armorName = kwargs.get('armorName', 'none')
    if armorName == 'none':
        arm = {'armor class': 10 + conMod + dexMod}
    else:
        arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'greataxe')
    wpn = weapon(weaponName, stats, lvl)

    # brutal critical
    if lvl >= 17:
        wpn['damage'] += ' + 3'
    elif lvl >= 13:
        wpn['damage'] += ' + 2'
    elif lvl >= 9:
        wpn['damage'] += ' + 1'

    reckless_attack = True
    if lvl >= 2 and reckless_attack:
        wpn['attack bonus'] += 4
        arm['armor class'] -= 4

    pc = {
        'name': name,
        'class': 'barbarian',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': hitPointsEquation(lvl, 'd12', stats), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'],
        'actions': {
            'Attack': newAction(attacks=attacks*[wpn])
        },
        'bonus actions': {
            'None': newAction(),
            'Rage': newAction(
                effect=newEffect(duration=10, hpmultiplier=1.5, actions={'Attack': {'damage': '{:d}'.format(rageBonus)}}), 
                resources={'Rage': -1})
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing='d12 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest'),
            'Rage': newResource(uses=rages, recharge='long rest')
        }
    }

    if lvl >= 2: # Danger Sense
        pc['armor class'] += 1

    if lvl >= 11: # Relentless Rage
        pc['hit points multiplier'] *= 1.10

    return pc

def bardPC(name='Bard', **kwargs):
    lvl = int(kwargs.get('lvl', 1))
    pb = proficiencyBonus(lvl)

    # stats
    stats = kwargs.get('stats', [10,14,12,10,12,16])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)
    
    asiLvl = [4,8,12,16,19]
    asi = kwargs.get('asi', 2*[newASI(charisma=2)] + 3*[newASI(intelligence=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])

    conMod = abilityModifier(stats['Constitution'])
    spMod = abilityModifier(stats['Charisma'])

    # equipment
    if lvl >= 5:
        armorName = kwargs.get('armorName', 'studded leather')
    else:
        armorName = kwargs.get('armorName', 'leather')
    arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'rapier')
    wpn = weapon(weaponName, stats, lvl)

    pc = {
        'name': name,
        'class': 'bard',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': '8 + {:d}d8 + {:d}'.format(lvl-1, conMod*lvl), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'] + 2, # shield
        'actions': {
            'Attack': newAction(attacks=[wpn])
        },
        'bonus actions': {
            'None': newAction(),
            'Bardic Inspiration': newAction(
                acbonus=[1,2,3,4][np.sum(np.array([1,5,10,15]) <= lvl)-1], 
                resources={'Bardic Inspiration': -1}, 
                comment='bardic inspiration die = {:}'.format(['1d6','1d8','1d10','1d12'][np.sum(np.array([1,5,10,15]) <= lvl)-1])
            )
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing='d8 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest'),
            'Bardic Inspiration': newResource(uses=spMod, recharge='long rest')
        }
    }

    # add spellcasting
    spSlots = spellSlots(lvl)
    spDmg = spellDamage(lvl)
    spHeal = spellHealing(lvl)
    for i in range(10):
        if spSlots[i] > 0:
            resName = 'Spell Slot ({:d})'.format(i)
            pc['resources'][resName] = newResource(uses=spSlots[i], recharge='long rest')
            actName = 'Cast a Spell ({:d})'.format(i)
            pc['actions'][actName] = newAction(attacks=[{'damage': spDmg[i], 'attack bonus': spMod + pb}], resources={resName: -1})

            actName = 'Cast a Spell ({:d}) - Healing'.format(i)
            #pc['actions'][actName] = newAction(healing=spHeal[i], resources={resName: -1})

    if lvl >= 2: # Song of Rest
        pc['short rests']['Song of Rest'] = newAction(healing=['1d6','1d8','1d10','1d12'][np.sum(np.array([2,9,13,17]) <= lvl)-1])

    if lvl >= 5: # Font of Inspiration
        pc['resources']['Bardic Inspiration'] = newResource(uses=spMod, recharge='short rest')
    
    return pc

def clericPC(name='Cleric', **kwargs):
    lvl = int(kwargs.get('lvl', 1))
    pb = proficiencyBonus(lvl)

    # stats
    stats = kwargs.get('stats', [14,14,12,10,16,10])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)
    
    asiLvl = [4,8,12,16,19]
    asi = kwargs.get('asi', 2*[newASI(wisdom=2)] + 3*[newASI(strength=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])

    conMod = abilityModifier(stats['Constitution'])
    spMod = abilityModifier(stats['Wisdom'])

    # equipment
    if lvl >= 5:
        armorName = kwargs.get('armorName', 'half plate')
    else:
        armorName = kwargs.get('armorName', 'scale mail')
    arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'mace')
    wpn = weapon(weaponName, stats, lvl)

    pc = {
        'name': name,
        'class': 'cleric',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': '8 + {:d}d8 + {:d}'.format(lvl-1, conMod*lvl), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'] + 2, # shield
        'actions': {
            'Attack': newAction(attacks=[wpn])
        },
        'bonus actions': {
            'None': newAction()
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing='d8 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest')
        }
    }

    # add spellcasting
    spSlots = spellSlots(lvl)
    spDmg = spellDamage(lvl)
    spHeal = spellHealing(lvl)
    for i in range(10):
        if spSlots[i] > 0:
            resName = 'Spell Slot ({:d})'.format(i)
            pc['resources'][resName] = newResource(uses=spSlots[i], recharge='long rest')
            actName = 'Cast a Spell ({:d})'.format(i)
            pc['actions'][actName] = newAction(attacks=[{'damage': spDmg[i], 'attack bonus': spMod + pb}], resources={resName: -1})

            actName = 'Cast a Spell ({:d}) - Healing'.format(i)
            #pc['actions'][actName] = newAction(healing=spHeal[i], resources={resName: -1})
            
    if lvl >= 2: # Channel Divinity
        pc['resources']['Channel Divinity'] = newResource(uses=np.sum(np.array([2,6,18]) <= lvl), recharge='short rest')

    if lvl >= 8: # Potent Spellcasting
        pc['actions']['Cast a Spell (0)'] = newAction(attacks=[{'damage': spDmg[0] + ' + {:d}'.format(spMod), 'attack bonus': spMod + pb}], resources={'Spell Slot (0)': -1})
    
    return pc

def druidPC(name='Druid', **kwargs):
    lvl = int(kwargs.get('lvl', 1))
    pb = proficiencyBonus(lvl)

    # stats
    stats = kwargs.get('stats', [10,14,14,12,16,10])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)
    
    asiLvl = [4,8,12,16,19]
    asi = kwargs.get('asi', 2*[newASI(wisdom=2)] + 3*[newASI(dexterity=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])

    conMod = abilityModifier(stats['Constitution'])
    spMod = abilityModifier(stats['Wisdom'])

    # equipment
    if lvl >= 5:
        armorName = kwargs.get('armorName', 'scale mail')
    else:
        armorName = kwargs.get('armorName', 'leather')
    arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'scimitar')
    wpn = weapon(weaponName, stats, lvl)

    pc = {
        'name': name,
        'class': 'druid',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': '8 + {:d}d8 + {:d}'.format(lvl-1, conMod*lvl), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'] + 2, # shield
        'actions': {
            'Attack': newAction(attacks=[wpn])
        },
        'bonus actions': {
            'None': newAction()
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing='d8 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest')
        }
    }

    # add spellcasting
    spSlots = spellSlots(lvl)
    spDmg = spellDamage(lvl)
    spHeal = spellHealing(lvl)
    for i in range(10):
        if spSlots[i] > 0:
            resName = 'Spell Slot ({:d})'.format(i)
            pc['resources'][resName] = newResource(uses=spSlots[i], recharge='long rest')
            actName = 'Cast a Spell ({:d})'.format(i)
            pc['actions'][actName] = newAction(attacks=[{'damage': spDmg[i], 'attack bonus': spMod + pb}], resources={resName: -1})
            
            actName = 'Cast a Spell ({:d}) - Healing'.format(i)
            #pc['actions'][actName] = newAction(healing=spHeal[i], resources={resName: -1})
    
    return pc

def fighterPC(name='Fighter', **kwargs):
    lvl = int(kwargs.get('lvl', 1))

    # stats
    stats = kwargs.get('stats', [16,12,14,10,12,10])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)
    
    asiLvl = [4,6,8,12,14,16,19]
    asi = kwargs.get('asi', 2*[newASI(strength=2)] + 3*[newASI(constitution=2)] + 2*[newASI(wisdom=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])
    
    conMod = abilityModifier(stats['Constitution'])
    attacks = np.sum(np.array([1,5,11,17]) <= lvl)

    # equipment
    if lvl >= 5:
        armorName = kwargs.get('armorName', 'plate')
    else:
        armorName = kwargs.get('armorName', 'chain mail')
    arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'greatsword')
    wpn = weapon(weaponName, stats, lvl)

    # fighting style
    fightingstyle='defense'
    if fightingstyle == 'archery':
        x = 1
    elif fightingstyle == 'defense':
        arm['armor class'] += 1
    elif fightingstyle == 'dueling':
        x = 1
    elif fightingstyle == 'great weapon fighting':
        x = 1
    elif fightingstyle == 'two-weapon fighting':
        x = 1

    pc = {
        'name': name,
        'class': 'fighter',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': '10 + {:d}d10 + {:d}'.format(lvl-1, conMod*lvl), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'],
        'actions': {
            'Attack': newAction(attacks=attacks*[wpn]),
            'Action Surge (Attack)': newAction(attacks=2*attacks*[wpn], resources={'Action Surge': -1})
        },
        'bonus actions': {
            'None': newAction(),
            'Second Wind': newAction(healing='1d10 + {:d}'.format(lvl), resources={'Second Wind': -1})
        },
        'reactions': {
            'None': newAction(),
            'Indomitable': newAction(acbonus=4, resource={'Indomitable': -1}, comment='This is not an reaction, but I have no other way of handling it right now')
        },
        'short rests': {
            'hit dice': newAction(healing='d10 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest'),
            'Second Wind': newResource(uses=1, recharge='short rest'),
            'Action Surge': newResource(uses=np.sum(np.array([2,17]) <= lvl), recharge='short rest'),
            'Indomitable': newResource(uses=np.sum(np.array([9,13,17]) <= lvl), recharge='long rest')
        }
    }

    return pc

def monkPC(name='Monk', **kwargs):
    lvl = int(kwargs.get('lvl', 1))

    # stats
    stats = kwargs.get('stats', [10,16,14,10,16,10])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)
    
    asiLvl = [4,8,12,16,19]
    asi = kwargs.get('asi', 2*[newASI(dexterity=2),newASI(wisdom=2)] + [newASI(constitution=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])
    
    strMod = abilityModifier(stats['Strength'])
    dexMod = abilityModifier(stats['Dexterity'])
    conMod = abilityModifier(stats['Constitution'])
    wisMod = abilityModifier(stats['Wisdom'])

    attacks = np.sum(np.array([1,5]) <= lvl)

    # equipment
    armorName = kwargs.get('armorName', 'none')
    if armorName == 'none':
        arm = {'armor class': 10 + wisMod + dexMod}
    else:
        arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'quarterstaff')
    wpn   = monkWeapon(weaponName, stats, lvl)
    unarm = monkWeapon('none', stats, lvl)

    pc = {
        'name': name,
        'class': 'monk',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': '8 + {:d}d8 + {:d}'.format(lvl-1, conMod*lvl), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'],
        'actions': {
            'Attack': newAction(attacks=attacks*[wpn])
        },
        'bonus actions': {
            'None': newAction(),
            'Martial Arts': newAction(attacks=[unarm], requires={'action': 'Attack'})
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing='d8 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest'),
        }
    }

    if lvl >= 2:
        pc['resources']['ki'] = newResource(uses=lvl, recharge='short rest')
        pc['bonus actions']['Flurry of Blows'] = newAction(attacks=2*[unarm], resources={'ki': -1}, requires={'action': 'Attack'})
        #pc['bonus actions']['Patient Defense'] = newAction(acbonus=4, resources={'ki': -1})

    if lvl >= 3: # Ki Fueled Attack
        pc['bonus actions']['Ki Fueled Attack'] = newAction(attacks=[wpn], requires={'action': 'Empty Body'})
    
    if lvl >= 7: # Evasion
        pc['armor class'] += 2

    if lvl >= 14: # Diamond Soul
        pc['armor class'] += 4

    if lvl >= 18:
        
        pc['actions']['Empty Body'] = newAction(
            effect=newEffect(duration=10, hpmultiplier=2.0, acbonus=4, abbonus=4), 
            resources={'ki': -4})

    return pc

def paladinPC(name='Paladin', **kwargs):
    lvl = int(kwargs.get('lvl', 1))

    # stats
    stats = kwargs.get('stats', [16,12,14,10,12,14])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)

    asiLvl = [4,8,12,16,19]
    asi = kwargs.get('asi', 2*[newASI(strength=2)] + 2*[newASI(charisma=2)] + [newASI(constitution=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])
    
    conMod = abilityModifier(stats['Constitution'])
    spMod = abilityModifier(stats['Charisma'])

    # equipment
    if lvl >= 5:
        armorName = kwargs.get('armorName', 'plate')
    else:
        armorName = kwargs.get('armorName', 'chain mail')
    arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'greatsword')
    wpn = weapon(weaponName, stats, lvl)
    if lvl >= 11: #Improved Divine Smite
        wpn['damage'] += ' + 1d8'
    
    attacks = np.sum(np.array([1,5]) <= lvl)
    pc = {
        'name': name,
        'class': 'paladin',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': '10 + {:d}d10 + {:d}'.format(lvl-1, conMod*lvl), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'] + 1, # defense fighting style
        'actions': {
            'Attack': newAction(attacks=attacks*[wpn]),
            'Lay on Hands': newAction(healing='{:d}'.format(5), resources={'Lay on Hands': -5})
        },
        'bonus actions': {
            'None': newAction()
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing='d10 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest'),
            'Lay on Hands': newResource(uses=5*lvl, recharge='long rest')
        }
    }

    if lvl >= 2:
        # add spellcasting
        spSlots = spellSlots(int(np.ceil(lvl/2)))
        spDmg = spellDamage(lvl)
        smDmg = ['0','2d8','3d8','4d8','5d8','5d8']
        for i in range(1, 6):
            if spSlots[i] > 0:
                resName = 'Spell Slot ({:d})'.format(i)
                pc['resources'][resName] = newResource(uses=spSlots[i], recharge='long rest')
                actName = 'Attack - Smite ({:d})'.format(i)
                pc['actions'][actName] = newAction(attacks=attacks*[{'damage': wpn['damage'] + ' + ' + smDmg[i], 'attack bonus': wpn['attack bonus']}], 
                    resources={resName: -1})

                actName = 'Bonus Spell ({:d})'.format(i)
                pc['bonus actions'][actName] = newAction(attacks=[{'damage': spDmg[i], 'attack bonus': wpn['attack bonus']}], 
                    resources={resName: -1},
                    requires={'action': [
                        'Attack',
                        'Attack - Smite (1)',
                        'Attack - Smite (2)',
                        'Attack - Smite (3)',
                        'Attack - Smite (4)',
                        'Attack - Smite (5)'
                    ]})
    
    if lvl >= 3: # Channel Divinity
        pc['resources']['Channel Divinity'] = newResource(uses=1, recharge='short rest')

    if lvl >= 6: # Aura of Protection
        pc['armor class'] += max(spMod/2, 1)
    
    return pc

def rangerPC(name='Ranger', **kwargs):
    lvl = int(kwargs.get('lvl', 1))

    # stats
    stats = kwargs.get('stats', [10,16,14,10,14,12])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)
    
    asiLvl = [4,8,12,16,19]
    asi = kwargs.get('asi', 2*[newASI(dexterity=2)] + 2*[newASI(wisdom=2)] + [newASI(constitution=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])
    
    conMod = abilityModifier(stats['Constitution'])
    spMod = abilityModifier(stats['Wisdom'])

    # equipment
    if lvl >= 5:
        armorName = kwargs.get('armorName', 'studded leather')
    else:
        armorName = kwargs.get('armorName', 'leather')
    arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'longbow')
    wpn = weapon(weaponName, stats, lvl)
    wpn['attack bonus'] += 2 # archery fighting style
    
    attacks = np.sum(np.array([1,5]) <= lvl)

    pc = {
        'name': name,
        'class': 'ranger',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': '10 + {:d}d10 + {:d}'.format(lvl-1, conMod*lvl), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'],
        'actions': {
            'Attack': newAction(attacks=attacks*[wpn])
        },
        'bonus actions': {
            'None': newAction()
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing='d10 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest')
        }
    }

    if lvl >= 2:
        # add spellcasting
        spDmg = spellDamage(lvl)
        spSlots = spellSlots(int(np.ceil(lvl/2)))
        for i in range(1, 6):
            if spSlots[i] > 0:
                resName = 'Spell Slot ({:d})'.format(i)
                pc['resources'][resName] = newResource(uses=spSlots[i], recharge='long rest')
                actName = 'Bonus Spell ({:d})'.format(i)
                pc['bonus actions'][actName] = newAction(attacks=[{'damage': spDmg[i], 'attack bonus': wpn['attack bonus']}], 
                    resources={resName: -1},
                    requires={'action': ['Attack']})
    
    return pc

def roguePC(name='Rogue', **kwargs):
    lvl = int(kwargs.get('lvl', 1))
    pb = proficiencyBonus(lvl)

    # stats
    stats = kwargs.get('stats', [10,16,14,12,12,10])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)
    
    asiLvl = [4,8,10,12,16,19]
    asi = kwargs.get('asi', 2*[newASI(dexterity=2)] + 2*[newASI(wisdom=2)] + 2*[newASI(intelligence=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])
    
    conMod = abilityModifier(stats['Constitution'])
    
    sneakDice = int(np.ceil(lvl/2))

    # equipment
    if lvl >= 5:
        armorName = kwargs.get('armorName', 'studded leather')
    else:
        armorName = kwargs.get('armorName', 'leather')
    arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'shortbow')
    wpn = weapon(weaponName, stats, lvl)
    wpn['damage'] += ' + {:d}d6'.format(sneakDice)
    wpn['attack bonus'] += 4
    
    pc = {
        'name': name,
        'class': 'rogue',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': '8 + {:d}d8 + {:d}'.format(lvl-1, conMod*lvl), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'],
        'actions': {
            'Attack': newAction(attacks=[wpn], comment='Extra +4 to attack bonus comes from advantage from hiding each round.')
        },
        'bonus actions': {
            'None': newAction()
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing='d8 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest')
        }
    }
    if lvl >= 5:
        pc['reactions']['Uncanny Dodge'] = newAction(hpmultiplier=1.20)
    
    if lvl >= 7: # Evasion
        pc['armor class'] += 2

    if lvl >= 15: # Slippery Mind
        pc['armor class'] += 2
    
    return pc

def sorcererPC(name='Sorcerer', **kwargs):
    lvl = int(kwargs.get('lvl', 1))
    pb = proficiencyBonus(lvl)

    # stats
    stats = kwargs.get('stats', [10,14,12,10,12,16])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)
    
    asiLvl = [4,8,12,16,19]
    asi = kwargs.get('asi', 2*[newASI(charisma=2)] + 3*[newASI(wisdom=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])
    
    dexMod = abilityModifier(stats['Dexterity'])
    conMod = abilityModifier(stats['Constitution'])
    spMod = abilityModifier(stats['Charisma'])

    # equipment
    armorName = kwargs.get('armorName', 'mage armor')
    if armorName == 'mage armor':
        arm = {'armor class': 13 + dexMod}
    else:
        arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'dagger')
    wpn = weapon(weaponName, stats, lvl)

    pc = {
        'name': name,
        'class': 'sorcerer',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': '6 + {:d}d6 + {:d}'.format(lvl-1, conMod*lvl), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'],
        'actions': {
            'Attack': newAction(attacks=[wpn])
        },
        'bonus actions': {
            'None': newAction()
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing='d6 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest'),
        }
    }

    # add spellcasting
    spDmg = spellDamage(lvl)
    spSlots = spellSlots(lvl)
    if armorName == 'mage armor':
        spSlots[1] -= 1
    if lvl >= 2:
        spSlots = sorcererFlexibleCasting(lvl, spSlots)
    for i in range(10):
        if spSlots[i] > 0:
            resName = 'Spell Slot ({:d})'.format(i)
            pc['resources'][resName] = newResource(uses=spSlots[i], recharge='long rest')
            actName = 'Cast a Spell ({:d})'.format(i)
            pc['actions'][actName] = newAction(attacks=[{'damage': spDmg[i], 'attack bonus': spMod + pb}], resources={resName: -1})

            if i <= 3:
                actName = 'Spell Reaction ({:d})'.format(i)
                #pc['reactions'][actName] = newAction(acbonus=3, resources={resName: -1}, comment='Shield or Counterspell')  
    
    return pc

def warlockPC(name='Warlock', **kwargs):
    lvl = int(kwargs.get('lvl', 1))
    pb = proficiencyBonus(lvl)

    # stats
    stats = kwargs.get('stats', [10,14,12,10,12,16])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)
    
    asiLvl = [4,8,12,16,19]
    asi = kwargs.get('asi', 2*[newASI(charisma=2)] + 3*[newASI(wisdom=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])
    
    dexMod = abilityModifier(stats['Dexterity'])
    conMod = abilityModifier(stats['Constitution'])
    spMod = abilityModifier(stats['Charisma'])

    # equipment
    armorName = kwargs.get('armorName', 'leather')
    if armorName == 'mage armor':
        arm = {'armor class': 13 + dexMod}
    else:
        arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'dagger')
    wpn = weapon(weaponName, stats, lvl)

    pc = {
        'name': name,
        'class': 'warlock',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': '8 + {:d}d8 + {:d}'.format(lvl-1, conMod*lvl), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'],
        'actions': {
            'Attack': newAction(attacks=[wpn])
        },
        'bonus actions': {
            'None': newAction()
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing='d8 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest'),
        }
    }

    # add spellcasting actions
    ctrpMult = np.sum(np.array([1,5,11,17]) <= lvl)
    pc['actions']['Cast a Spell (0)'] = newAction(attacks=ctrpMult*[{'damage': '1d10 + {:d}'.format(spMod), 'attack bonus': spMod + pb}]) 

    spDmg = spellDamage(lvl)
    pmlvl = int(min(np.ceil(lvl/2), 5))
    pmSlots = np.sum(np.array([1,2,11,17]) <= lvl)
    resName = 'Spell Slot ({:d})'.format(pmlvl)
    pc['resources'][resName] = newResource(uses=pmSlots, recharge='short rest')
    actName = 'Cast a Spell ({:d})'.format(pmlvl)
    pc['actions'][actName] = newAction(attacks=[{'damage': spDmg[pmlvl], 'attack bonus': spMod + pb}], resources={resName: -1}) 

    #actName = 'Reaction Spell ({:d})'.format(pmlvl)
    #pc['reactions'][actName] = newAction(acbonus=3, resources={resName: -1}, comment='Shield or Counterspell') 

    if lvl >= 11:
        spLvl = 6
        resName = 'Mystic Arcanum ({:d})'.format(spLvl)
        pc['resources'][resName] = newResource(uses=1, recharge='long rest')
        actName = 'Cast a Spell ({:d})'.format(spLvl)
        pc['actions'][actName] = newAction(attacks=[{'damage': spDmg[spLvl], 'attack bonus': spMod + pb}], resources={resName: -1}) 

    if lvl >= 13:
        spLvl = 7
        resName = 'Mystic Arcanum ({:d})'.format(spLvl)
        pc['resources'][resName] = newResource(uses=1, recharge='long rest')
        actName = 'Cast a Spell ({:d})'.format(spLvl)
        pc['actions'][actName] = newAction(attacks=[{'damage': spDmg[spLvl], 'attack bonus': spMod + pb}], resources={resName: -1}) 

    if lvl >= 15:
        spLvl = 8
        resName = 'Mystic Arcanum ({:d})'.format(spLvl)
        pc['resources'][resName] = newResource(uses=1, recharge='long rest')
        actName = 'Cast a Spell ({:d})'.format(spLvl)
        pc['actions'][actName] = newAction(attacks=[{'damage': spDmg[spLvl], 'attack bonus': spMod + pb}], resources={resName: -1}) 

    if lvl >= 17:
        spLvl = 9
        resName = 'Mystic Arcanum ({:d})'.format(spLvl)
        pc['resources'][resName] = newResource(uses=1, recharge='long rest')
        actName = 'Cast a Spell ({:d})'.format(spLvl)
        pc['actions'][actName] = newAction(attacks=[{'damage': spDmg[spLvl], 'attack bonus': spMod + pb}], resources={resName: -1}) 
    
    return pc

def wizardPC(name='Wizard', **kwargs):
    lvl = int(kwargs.get('lvl', 1))
    pb = proficiencyBonus(lvl)

    # stats
    stats = kwargs.get('stats', [10,14,12,16,12,10])
    if isinstance(stats, list):
        stats = abilityScores_l2d(stats)
    
    asiLvl = [4,8,12,16,19]
    asi = kwargs.get('asi', 2*[newASI(intelligence=2)] + 3*[newASI(wisdom=2)])
    if asi:
        for i in range(min(len(asi), len(asiLvl))):
            if lvl >= asiLvl[i]:
                stats = applyASI(stats, asi[i])
    
    dexMod = abilityModifier(stats['Dexterity'])
    conMod = abilityModifier(stats['Constitution'])
    spMod = abilityModifier(stats['Intelligence'])

    # equipment
    armorName = kwargs.get('armorName', 'mage armor')
    if armorName == 'mage armor':
        arm = {'armor class': 13 + dexMod}
    else:
        arm = armor(armorName, stats)
    weaponName = kwargs.get('weaponName', 'dagger')
    wpn = weapon(weaponName, stats, lvl)
    pc = {
        'name': name,
        'class': 'wizard',
        'level': lvl,
        'ability scores': stats,
        'proficiency bonus': proficiencyBonus(lvl),
        'hit points': '6 + {:d}d6 + {:d}'.format(lvl-1, conMod*lvl), 
        'hit points multiplier': 1.0,
        'armor class': arm['armor class'],
        'actions': {
            'Attack': newAction(attacks=[wpn])
        },
        'bonus actions': {
            'None': newAction()
        },
        'reactions': {
            'None': newAction()
        },
        'short rests': {
            'hit dice': newAction(healing='d6 + {:d}'.format(conMod), resources={'hit dice': -1})
        },
        'long rests': {
            'None': newAction()
        },
        'resources': {
            'hit dice': newResource(uses=lvl, recharge='long rest')
        }
    }
    
    # add spellcasting
    spDmg = spellDamage(lvl)
    spSlots = spellSlots(lvl)
    if armorName == 'mage armor':
        spSlots[1] -= 1
    spSlots = wizardArcaneRecovery(lvl, spSlots, spDmg)
    for i in range(10):
        if spSlots[i] > 0:
            resName = 'Spell Slot ({:d})'.format(i)
            pc['resources'][resName] = newResource(uses=spSlots[i], recharge='long rest')
            actName = 'Cast a Spell ({:d})'.format(i)
            pc['actions'][actName] = newAction(attacks=[{'damage': spDmg[i], 'attack bonus': spMod + pb}], resources={resName: -1})     

            if i <= 3 and i >= 1:
                actName = 'Spell Reaction ({:d})'.format(i)
                #pc['reactions'][actName] = newAction(acbonus=3, resources={resName: -1}, comment='Shield or Counterspell')

    return pc







