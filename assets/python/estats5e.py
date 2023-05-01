import numpy as np

P0 = 0.65  # Baseline chance to hit
AB0 = 3    # Baseline attack bonus
AC0 = 12   # Baseline armor class
SB0 = -2   # Baseline saving throw bonus
DC0 = 12   # Baseline save DC

norm    = np.power(P0,  0.5)
norminv = np.power(P0, -0.5)
scale   = (0.05/P0)

def effDPR(DPR, AB, method='linear'):
    """Returns effective damage per round
    DPR -- average damage per round
    AB -- attack bonus
    method -- calculation method
    """
    if method == 'exp':
        return norm*DPR*np.power(1 + scale, AB - AB0)
    elif method == 'linear':
        return norm*DPR*(1 + scale*(AB - AB0))

def effHP(HP, AC, method='linear'):
    """Returns effective damage per round
    HP -- hit points
    AC -- armor class
    method -- calculation method
    """
    if method == 'exp':
        return norminv*HP*np.power(1 + scale, AC - AC0)
    elif method == 'linear':
        return norminv*HP*(1 + scale*(AC - AC0))

def effXP(hp, ac, dpr, ab, method='linear', ctype='NPC'):
    """Returns effective damage per round
    hp -- hit points
    ac -- armor class
    dpr -- average damage per round
    ab -- attack bonus
    method -- calculation method
    ctype -- creature type ('NPC' or 'PC')
    """
    if ctype.upper() == 'NPC':
        c = 0.25
    elif ctype.upper() == 'PC':
        c = 1.00
    else:
        c = np.nan

    if method == 'exp':
        return c*hp*dpr*np.power(1 + scale, ac + ab - (AC0 + AB0))
    elif method == 'linear':
        return c*hp*dpr*(1 + scale*(ac + ab - (AC0 + AB0)))
    elif method == 'quadratic':
        return c*hp*dpr*(1 + scale*(ac - AC0))*(1 + scale*(ab - AB0))