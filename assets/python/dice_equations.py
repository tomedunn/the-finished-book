"""Parsing dice equations and extracting average and variance values from it.

Functions:

    reconstruct_equation(list) -> string
    roll_average(string) -> float
    roll_sigma(string) -> float
    roll_variance(string) -> float
    tokenize_equation(string) -> list
"""

import numpy as np
import re

RE_DICE_ELEMENT = re.compile(
    r'(?P<die_count>\d*)d(?P<die_sides>\d+)'
)

RE_DEQ_ELEMENT = re.compile(
    r'\s*'
    r'(?P<opperator>[\-\+])'
    r'|(?P<dice>\d*d\d+)'
    r'|(?P<constant>\d+)'
)

def _elem_average(elem):
    """Returns average (mean) for a single element dice equation."""
    elem_type = elem[0]
    match elem_type:
        case 'dice':
            match = RE_DICE_ELEMENT.match(elem[1])
            die_count = int(match.group('die_count')) if match.group('die_count') else 1
            die_ave = 0.5*(int(match.group('die_sides')) + 1)
            return (elem_type, die_count*die_ave)
        case 'constant':
            return (elem_type, float(elem[1]))
        case _:
            return elem

def _elem_variance(elem):
    """Returns variance for a single element dice equation."""
    elem_type = elem[0]
    match elem_type:
        case 'dice':
            match = RE_DICE_ELEMENT.match(elem[1])
            die_count = int(match.group('die_count')) if match.group('die_count') else 1
            die_sides = int(match.group('die_sides'))
            die_var = (die_sides*die_sides - 1)/12.0
            return (elem_type, die_count*die_var)
        case 'constant':
            return (elem_type, 0.0)
        case _:
            return elem


def reconstruct_equation(dice_tokens):
    """Reconstructs a dice equation string from tokens
    
    Args:
        dice_tokens: A list of tuples representing a dice equation.

    Returns:
        A string that represent the dice equation.
    """
    """"""
    return ' '.join([e[1] for e in dice_tokens])


def tokenize_equation(dice_equation):
    """Splits a dice equation into its component pieces.
    
    Args:
        dice_equation: A string representing a dice equation.

    Returns:
        A list of tuples that represent the dice equation components.
    """
    """"""
    deq_elems = []
    for match in RE_DEQ_ELEMENT.findall(dice_equation):
        for pair in zip(RE_DEQ_ELEMENT.groupindex.keys(), match):
            if pair[1] != '':
                deq_elems.append(pair)
    return deq_elems


def roll_average(dice_equation):
    """Calculates average (mean) for a dice equation.
    
    Args:
        dice_equation: A string representing a dice equation.

    Returns:
        A float representing the mean of the given dice equation.
    """
    if isinstance(dice_equation, str):
        deq_elems = tokenize_equation(dice_equation)
    else:
        deq_elems = dice_equation
    deq_elems_ave = [_elem_average(e) for e in deq_elems]
    elem = deq_elems_ave.pop(0)
    average = elem[1]
    it = iter(deq_elems_ave)
    for elem in it:
        if elem[1] == '+':
            average += next(it)[1]
        else:
            average -= next(it)[1]
    return average


def roll_variance(dice_equation):
    """Calculates variance for a dice equation.
    
    Args:
        dice_equation: A string representing a dice equation.

    Returns:
        A float representing the variance of the given dice equation.
    """
    if isinstance(dice_equation, str):
        deq_elems = tokenize_equation(dice_equation)
    else:
        deq_elems = dice_equation
    deq_elems_var = [_elem_variance(e) for e in deq_elems]
    variance = np.sum([e[1] for e in deq_elems_var if e[0] == 'dice'])
    return variance


def roll_sigma(dice_equation):
    """Calculates standard deviation for a dice equation.
    
    Args:
        dice_equation: A string representing a dice equation.

    Returns:
        A float representing the standard deviation of the given dice equation.
    """
    return np.sqrt(roll_variance(dice_equation))