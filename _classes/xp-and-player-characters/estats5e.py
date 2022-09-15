import numpy as np

norm    = np.power(0.6,  0.5)
norminv = np.power(0.6, -0.5)
scale   = (0.05/0.6)

def effDPR(DPR, AB, method='linear'):
    """Returns effective damage per round
    DPR -- average damage per round
    AB -- attack bonus
    method -- calculation method
    """
    if method == 'exp':
        return norm*DPR*np.power(1 + scale, AB - 3)
    elif method == 'linear':
        return norm*DPR*(1 + scale*(AB - 3))

def effHP(HP, AC, method='linear'):
    """Returns effective damage per round
    HP -- hit points
    AC -- armor class
    method -- calculation method
    """
    if method == 'exp':
        return norminv*HP*np.power(1 + scale, AC - 13)
    elif method == 'linear':
        return norminv*HP*(1 + scale*(AC - 13))

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
        return c*hp*dpr*np.power(1 + scale, ac + ab - 16)
    elif method == 'linear':
        return c*hp*dpr*(1 + scale*(ac + ab - 16))
    elif method == 'quadratic':
        return c*hp*dpr*(1 + scale*(ac - 13))*(1 + scale*(ab - 3))