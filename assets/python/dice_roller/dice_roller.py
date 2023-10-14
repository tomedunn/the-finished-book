from dice_roller.lexer import Lexer
from dice_roller.parser_ import Parser
from dice_roller.interpreter import Interpreter

class Dice_Roller:
    def __init__(self, eq_str):
        self.eq_str = eq_str
        self.tokens = Lexer(self.eq_str).generate_tokens()
        self.tree = Parser(self.tokens).parse()
        self.value = Interpreter().evaluate(self.tree)