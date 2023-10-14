import re
from dice_roller.tokens import *

token_specification = [
    ('DIE',         r'\d*d\d+'),      # die
    ('NUMBER',      r'\d+(\.\d*)?'),  # Integer or decimal number
    ('OPERATOR',    r'[\*\+\-\/]'),   # Mathematical operator
    ('PARENTHESES', r'[\(\)]'),       # Parentheses
    ('SPACE',       r'\s'),           # Space character
    ('MISMATCH',    r'.'),            # Any other character
]
tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

class Lexer:
    def __init__(self, text):
        self.text = re.finditer(tok_regex, text)
        self.advance()

    def advance(self):
        try:
            self.current_match = next(self.text)
        except StopIteration:
            self.current_match = None
    
    def generate_tokens(self):
        while self.current_match != None:
            match self.current_match.lastgroup:
                case 'NUMBER':
                    yield self.generate_number()
                case 'DIE':
                    yield self.generate_die()
                case 'OPERATOR':
                    yield self.generate_operator()
                case 'PARENTHESES':
                    yield self.generate_parentheses()
                case 'SPACE':
                    self.advance()
                case 'MISMATCH':
                    raise RuntimeError(f'{self.current_match.group()!r} unexpected')

    def generate_die(self):
        die_str = self.current_match.group()
        self.advance()
        return Token(TokenType.DIE, die_str)
    
    def generate_number(self):
        num_str = self.current_match.group()
        self.advance()
        return Token(TokenType.NUMBER, float(num_str))
    
    def generate_operator(self):
        op = self.current_match.group()
        self.advance()
        match op:
            case '+':
                return Token(TokenType.PLUS)
            case '-':
                return Token(TokenType.MINUS)
            case '*':
                return Token(TokenType.MULTIPLY)
            case '/':
                return Token(TokenType.DIVIDE) 
            
    def generate_parentheses(self):
        paren_str = self.current_match.group()
        self.advance()
        match paren_str:
            case '(':
                return Token(TokenType.LPAREN)
            case ')':
                return Token(TokenType.RPAREN)