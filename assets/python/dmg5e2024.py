"""Methods for calculating monster CR and XP.

Functions:

    monster_default_stats(float) -> dict
    monster_defensive_challenge_rating(float, float) -> float
    monster_offensive_challenge_rating(float, float) -> float
    monster_challenge_rating(float, float, float, float) -> float
"""

import numpy as np

def _find_nearest_loc(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

# encounter functions
def encounter_xp( *args ):
    if len(args) == 1:
        crs = args[0]
    else:
        crs = args
    
    return sum([monster_default_stats(cr)['XP'] for cr in crs])

def encounter_adjusted_xp(pc_levels, mon_crs):
    """Returns the encounter's adjusted XP
    pc_levels -- a list of the levels for each PC in the encounter
    mon_crs -- a list of the CRs for each monster in the encounter
    """
    return encounter_xp(mon_crs)*encounter_xp_multiplier(len(pc_levels), len(mon_crs))

def encounter_xp_multiplier(pc_count, npc_count):
    """Returns the encounter multiplier given by the DMG
    pc_count -- number of PCs in the encounter
    npc_count -- number of NPCs in the encounter
    """
    return 1.0

def encounter_difficulty( pc_levels, mon_crs ):
    enc_adj_xp = encounter_adjusted_xp(pc_levels, mon_crs)
    xp_thresholds = party_xp_thresholds(pc_levels)

    for k, v in xp_thresholds.items():
        if enc_adj_xp <= v: 
            return k
    return 'Very High'

# monster functions
MONSTER_DEFAULTS = {
    'CR': [0, 1/8, 1/4, 1/2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 
        14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'XP': [0, 25, 50, 100, 200, 450, 700, 1100, 1800, 2300, 2900, 3900, 5000, 
        5900, 7200, 8400, 10000, 11500, 13000, 15000, 18000, 20000, 22000, 25000, 
        33000, 41000, 50000, 62000, 75000, 90000, 105000, 120000, 135000, 155000],
    'PB': [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 
        5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9],
    'AC': [12, 13, 13, 13, 13, 13, 13, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 
        18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19],
    'HP mean': [3.5, 21.0, 42.5, 60.0, 78.0, 93.0, 108.0, 123.0, 138.0, 153.0, 
        168.0, 183.0, 198.0, 213.0, 228.0, 243.0, 258.0, 273.0, 288.0, 303.0, 
        318.0, 333.0, 348.0, 378.0, 423.0, 468.0, 513.0, 558.0, 603.0, 648.0, 
        693.0, 738.0, 783.0, 828.0],
    'AB': [2, 3, 3, 3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 8, 9, 
        10, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14],
    'DC': [12, 13, 13, 13, 13, 13, 13, 14, 15, 15, 15, 16, 16, 16, 17, 17, 18, 
        18, 18, 18, 19, 19, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23],
    'DPR mean': [0.5, 2.5, 4.5, 7.0, 11.5, 17.5, 23.5, 29.5, 35.5, 41.5, 47.5, 53.5, 
        59.5, 65.5, 71.5, 77.5, 83.5, 89.5, 95.5, 101.5, 107.5, 113.5, 119.5, 131.5, 
        149.5, 167.5, 185.5, 203.5, 221.5, 239.5, 257.5, 275.5, 293.5, 311.5]
}

def monster_default_stats(cr):
    """Returns default monster stats.
    cr -- challenge rating
    """
    id = _find_nearest_loc(MONSTER_DEFAULTS['CR'], cr)
    return {
        'CR': MONSTER_DEFAULTS['CR'][id],
        'XP': MONSTER_DEFAULTS['XP'][id],
        'PB': MONSTER_DEFAULTS['PB'][id],
        'AC': MONSTER_DEFAULTS['AC'][id],
        'HP mean': MONSTER_DEFAULTS['HP mean'][id],
        'AB': MONSTER_DEFAULTS['AB'][id],
        'DC': MONSTER_DEFAULTS['DC'][id],
        'DPR mean': MONSTER_DEFAULTS['DPR mean'][id]
    }

def monster_defensive_challenge_rating(hp, ac):
    """Returns offensive challenge rating
    hp -- average hit points
    ac -- armor class
    """
    id = _find_nearest_loc(MONSTER_DEFAULTS['HP mean'], hp)
    ac_delta = ac - MONSTER_DEFAULTS['AC'][id]
    id = int(max(0, min(33, id + np.fix(0.5*ac_delta))))
    return MONSTER_DEFAULTS['CR'][id]

def monster_offensive_challenge_rating(dpr, ab):
    """Returns offensive challenge rating
    dpr -- average damage per round
    ab -- attack bonus
    """
    id = _find_nearest_loc(MONSTER_DEFAULTS['DPR mean'], dpr)
    ab_delta = ab - MONSTER_DEFAULTS['AB'][id]
    id = int(max(0, min(33, id + np.fix(0.5*ab_delta))))
    return MONSTER_DEFAULTS['CR'][id]

def monster_challenge_rating(hp, ac, dpr, ab):
    """Returns challenge rating
    hp -- average hit points
    ac -- armor class
    dpr -- average damage per round
    ab -- attack bonus
    """
    d_cr = monster_defensive_challenge_rating(hp, ac)
    o_cr = monster_offensive_challenge_rating(dpr, ab)
    return 0.5*(o_cr + d_cr)

# player character functions
PC_XP_THRESHOLDS = {
    'level':    [  1,  2,   3,   4,   5,   6,   7,   8,   9,  10,   11,   12,   13,   14,   15,   16,   17,   18,   19,   20],
    'Low':      [ 50,100, 150, 250, 500, 600, 750,1000,1300,1600, 1900, 2200, 2600, 2900, 3300, 3800, 4500, 5000, 5500, 6400],
    'Moderate': [ 75,150, 225, 375, 750,1000,1300,1700,2000,2300, 2900, 3700, 4200, 4900, 5400, 6100, 7200, 8700,10700,13200],
    'High':     [100,200, 400, 500,1100,1400,1700,2100,2600,3100, 4100, 4700, 5400, 6200, 7800, 9800,11700,14200,17200,22000],
    'Daily':    [300,600,1200,1700,3500,4000,5000,6000,7500,9000,10500,11500,13500,15000,18000,20000,25000,27000,30000,40000],
}

def pc_xp_thresholds( level ):
    """Returns the XP thresholds for a PC of the given level.
    level -- the PC's level
    """
    id = _find_nearest_loc(PC_XP_THRESHOLDS['level'], level)
    return {
        'Low':      PC_XP_THRESHOLDS['Low'][id],
        'Moderate': PC_XP_THRESHOLDS['Moderate'][id],
        'High':     PC_XP_THRESHOLDS['High'][id],
        'Daily':    PC_XP_THRESHOLDS['Daily'][id],
    }

def party_xp_thresholds( *args ):
    xp_thresholds = {
        'Low':      0,
        'Moderate': 0,
        'High':     0,
        'Daily':    0,
    }
    if len(args) == 1:
        levels = args[0]
    else:
        levels = args
    
    for level in levels:
        pc = pc_xp_thresholds(level)
        for k in xp_thresholds.keys():
            xp_thresholds[k] += pc[k]
    return xp_thresholds

def party_xp_ranges( *args ):
    xp_thresholds = party_xp_thresholds(*args)
    xp_ranges = {
        'Low':      [xp_thresholds['Low'], xp_thresholds['Moderate']],
        'Moderate': [xp_thresholds['Moderate'], xp_thresholds['High']],
        'High':     [xp_thresholds['High'], xp_thresholds['Daily']/2],
    }
    return xp_ranges