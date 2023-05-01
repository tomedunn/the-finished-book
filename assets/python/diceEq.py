import numpy as np
import re

def __parse_equation(diceEqn):
    """Returns list of single element dice equations
    diceEqn -- string of dice equation
    """
    s = re.split(r'(\+|\-)', diceEqn)
    return s

def __elem_average(diceEqn):
    """Returns average (mean) for single element dice equation
    diceEqn -- string of single element dice equation
    """
    m = re.match(r'\s*(?:(\d*)d(\d+)|(\d+))\s*', diceEqn)
    if m.group(3):
        return int(m.group(3))
    else:
        n = int(m.group(1)) if m.group(1) else 1
        a = 0.5*(int(m.group(2)) + 1)
        return n*a

def __elem_sigma2(diceEqn):
    """Returns standard deviation squared for single element dice equation
    diceEqn -- string of single element dice equation
    """
    m = re.match(r'\s*(?:(\d*)d(\d+)|(\d+))\s*', diceEqn)
    if m.group(3):
        return 0
    else:
        n = int(m.group(1)) if m.group(1) else 1
        d = int(m.group(2))
        return n*(d*d - 1)/12.0

def rollAverage(diceEqn):
    """Returns average (mean) of dice equation
    diceEqn -- string of dice equation
    """
    s = __parse_equation(diceEqn)
    deq = s.pop(0)
    atot = __elem_average(deq)
    it = iter(s)
    for x in it:
        if x == '+':
            atot += __elem_average(next(it))
        else:
            atot -= __elem_average(next(it))
    return atot

def rollSigma(diceEqn):
    """Returns standard deviate of dice equation
    diceEqn -- string of dice equation
    """
    s = __parse_equation(diceEqn)
    deq = s.pop(0)
    atot = __elem_sigma2(deq)
    it = iter(s)
    for x in it:
        atot += __elem_sigma2(next(it))
    return np.sqrt(atot)