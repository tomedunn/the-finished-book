import numpy as np

XP_TARGETS = {
    'Easy': [25,50,75,125,250,300,350,450,550,600,800,1000,1100,1250,1400,1600,2000,2100,2400,2800],
    'Medium': [50,100,150,250,500,600,750,900,1100,1200,1600,2000,2200,2500,2800,3200,3900,4200,4900,5700],
    'Hard': [75,150,225,375,750,900,1100,1400,1600,1900,2400,3000,3400,3800,4300,4800,5900,6300,7300,8500],
    'Deadly': [100,200,400,500,1100,1400,1700,2100,2400,2800,3600,4500,5100,5700,6400,7200,8800,9500,10900,12700],
    'Encounter': [150,300,600,850,1750,2000,2500,3000,3750,4500,5250,5750,6750,7500,9000,10000,12500,13500,15000,20000],
    'Daily': [300,600,1200,1700,3500,4000,5000,6000,7500,9000,10500,11500,13500,15000,18000,20000,25000,27000,30000,40000],
}

# function definitions
def _split_number_into_groups( num, n_groups ):
    """Returns list with num split into n_groups.
    num -- int number to be split up
    n_groups -- int number of groups
    """
    num_base = int(np.floor(num/n_groups))
    groups = [num_base]*n_groups

    num_extra = num - num_base*n_groups
    for i in range(int(num_extra)):
        groups[i] += 1
    
    return groups

def calculate_encounters_per_day( level, diff ):
    """Returns float number of encounters.
    level -- int PC level
    diff -- string target encounter difficulty. Possible values: 'Easy', 'Medium', 'Hard', 'Deadly'
    """
    dif_XP = XP_TARGETS[diff][level-1]
    max_XP = XP_TARGETS['Daily'][level-1]
    #x = {'Easy': 12, 'Medium': 7, 'Hard': 4.5, 'Deadly': 3}
    return max_XP / dif_XP
    #return x[diff]

def calculate_rounds_per_encounter( level, diff ):
    """Returns float number of rounds.
    level -- int PC level
    diff -- string target encounter difficulty. Possible values: 'Easy', 'Medium', 'Hard', 'Deadly'
    """
    dif_XP = XP_TARGETS[diff][level-1]
    med_XP = XP_TARGETS['Medium'][level-1]
    return 3.0 * np.sqrt(dif_XP/med_XP)

def calculate_rounds_per_day( level, diff ):
    """Returns float number of rounds.
    level -- int PC level
    diff -- string target encounter difficulty. Possible values: 'Easy', 'Medium', 'Hard', 'Deadly'
    """
    return calculate_encounters_per_day(level, diff) * calculate_rounds_per_encounter(level, diff)

def create_adventuring_day_encounters( level, diff ):
    """Returns float number of rounds.
    level -- int PC level
    diff -- string target encounter difficulty. Possible values: 'Easy', 'Medium', 'Hard', 'Deadly'
    """
    rounds_per_enc = calculate_rounds_per_encounter(level, diff)
    encounters_per_day = calculate_encounters_per_day(level, diff)
    rounds_per_day = encounters_per_day * rounds_per_enc

    rounds = _split_number_into_groups(
        round(rounds_per_day), 
        round(encounters_per_day))

    return rounds

def create_adventuring_day( level, difficulty, short_rests ):
    # add encounters
    rounds = create_adventuring_day_encounters(level, difficulty)
    num_encounters = len(rounds)

    adventuring_day = [{'type': 'encounter', 'rounds': r} for r in rounds]
    
    # add short rests
    if short_rests > 0:
        encounters = _split_number_into_groups(num_encounters, (1 + short_rests))
        ins = 0
        for i in range(len(encounters)-1):
            ins += encounters[i]
            adventuring_day.insert(ins + i, {'type': 'short rest'})

    # finish day with long rest
    adventuring_day += [{'type': 'long rest'}]
    return adventuring_day