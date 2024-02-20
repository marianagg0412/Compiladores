from re import match
from Lang.token import (
    Token, TokenType
)

"""
The lexer is the one that identifies which token it is and returns it into the tree 
to be evaluated
"""


class Lexer:
    """
    We initialize variables to use in the class
    """
    def __init__(self, text: str) -> None:
        self.text = text
        self.pos = 0
        self.current_char = ""
        self._read_current_pos = 0
        self._read_char()

    """
    We assign the token and reads next character
    """
    def _read_char(self) -> None:
        if self._read_current_pos >= len(self.text):
            self.current_char = ""
        else:
            self.current_char = self.text[self._read_current_pos]
        self.pos = self._read_current_pos
        self._read_current_pos += 1

    """
    To avoid whitespaces
    """
    def _skip_whitespace(self) -> None:
        while self.current_char.isspace():
            self._read_char()

    """
    Evaluates each token and returns its type
    """
    def next_token(self):
        self._skip_whitespace()
        if match(r'^=$', self.current_char):
            token = Token(TokenType.ASSIGN, self.current_char)
        elif match(r'^\+$', self.current_char):
            token = Token(TokenType.PLUS, self.current_char)
        elif match(r'^,$', self.current_char):
            token = Token(TokenType.COMMA, self.current_char)
        elif match(r'^;$', self.current_char):
            token = Token(TokenType.SEMICOLON, self.current_char)
        elif match(r'^$', self.current_char):
            token = Token(TokenType.EOF, self.current_char)
        elif match(r'^\($', self.current_char):
            token = Token(TokenType.L_PAREN, self.current_char)
        elif match(r'^\)$', self.current_char):
            token = Token(TokenType.R_PAREN, self.current_char)
        elif match(r'^\{$', self.current_char):
            token = Token(TokenType.L_BRACE, self.current_char)
        elif match(r'^\}$', self.current_char):
            token = Token(TokenType.R_BRACE, self.current_char)
        elif match(r'^-$', self.current_char):
            token = Token(TokenType.MINUS, self.current_char)
        elif match(r'^/$', self.current_char):
            token = Token(TokenType.DIVISION, self.current_char)
        elif match(r'^\*$', self.current_char):
            token = Token(TokenType.MULTIPLICATION, self.current_char)
        elif match(r'^<$', self.current_char):
            token = Token(TokenType.LESS_THAN, self.current_char)
        elif match(r'^>$', self.current_char):
            token = Token(TokenType.GREATER_THAN, self.current_char)
        elif match(r'^\[$', self.current_char):
            token = Token(TokenType.L_BRACKET, self.current_char)
        elif match(r'^\]$', self.current_char):
            token = Token(TokenType.R_BRACKET, self.current_char)
        elif match(r'^!$', self.current_char):
            token = Token(TokenType.NOT, self.current_char)
        else:
            token = Token(TokenType.ILLEGAL, self.current_char)
        self._read_char()
        return token
