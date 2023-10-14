from dataclasses import dataclass
from icepool import d
import re

class NumberNode:
    def __init__(self, value_str):
        self.value_str = value_str
        self.value = int(self.value_str) @ d(1)

    def __repr__(self):
        return f'{self.value_str}'

class DieNode:
    def __init__(self, value_str):
        self.value_str = value_str
        m = re.match(r'^(?P<count>\d*)?[Dd](?P<sides>\d+)$', self.value_str)
        die_count = int(m.group('count')) if m.group('count') else 1
        die_sides = int(m.group('sides'))
        self.value = die_count @ d(die_sides)
    
    def __repr__(self):
        return f'{self.value_str}'

@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}+{self.node_b})'

@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}-{self.node_b})'

@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}*{self.node_b})'

@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}/{self.node_b})'

@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f'(+{self.node})'

@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f'(-{self.node})'