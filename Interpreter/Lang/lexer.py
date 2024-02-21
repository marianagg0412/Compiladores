from re import match
from Lang.token import (
    Token,
    TokenType,
    lookup_token_type
)

"""
El lexer es el que identifica cual token es y luego se pasa para generar el arbol y ser evaluado
"""


class Lexer:
    def __init__(self, source: str) -> None:
        self.source = source
        self.current_pos = 0
        self.current_char = ""
        self._read_current_pos = 0
        self._read_character()

    """
    Se asigna el token y se lee el siguiente caracter
    """

    def _read_character(self) -> None:
        if self._read_current_pos >= len(self.source):
            self.current_char = ""
        else:
            self.current_char = self.source[self._read_current_pos]
        self._current_pos = self._read_current_pos
        self._read_current_pos += 1
        """
        Para evitar espacios en blanco
        """

    def _skip_whitespace(self) -> None:
        while self.current_char.isspace():
            self._read_character()

    """
    peek_character lee el siguinte caracter sin necesidad 
    de avanzar en el cursor
    """

    def peek_character(self) -> str:
        if self._read_current_pos >= len(self.source):
            return ""
        else:
            return self.source[self._read_current_pos]

    """ para verificar que el caracter sea una letra
    """

    def is_letter(self, character: str) -> bool:
        return bool(match(r'^[a-záéíóúA-ZÁÉÍÓÚñÑ_]$', character))

    """Para evaluar si es un número
    """

    def is_number(self, character: str) -> bool:
        return bool(match(r'^\d$', character))

    """funcion para retornar si es un número
    """

    def _read_number(self) -> str:
        position = self._current_pos
        while self.is_number(self.current_char):
            self._read_character()
        return self.source[position:self._current_pos]

    def _read_identifier(self) -> str:
        position = self._current_pos
        # is_first_letter=True
        while self.is_letter(self.current_char) or \
                (self.is_number(self.current_char)):
            self._read_character()
            is_first_letter = False
        return self.source[position:self._current_pos]

    """ evalua cata token y devuelve su tipo"""

    def next_token(self):

        self._skip_whitespace()
        if match(r'^=$', self.current_char):
            if self.peek_character() == "=":
                self._read_character()
                token = Token(TokenType.EQ, "==")

            else:
                token = Token(TokenType.ASSIGN, self.current_char)

        elif match(r'^\+$', self.current_char):
            token = Token(TokenType.PLUS, self.current_char)
        elif match(r'^,$', self.current_char):
            token = Token(TokenType.COMMA, self.current_char)
        elif match(r'^;$', self.current_char):
            token = Token(TokenType.SEMICOLON, self.current_char)
        elif match(r'^!$', self.current_char):
            token = Token(TokenType.NOT, self.current_char)
        elif match(r'^$', self.current_char):
            token = Token(TokenType.EOF, self.current_char)
        elif match(r'^>$', self.current_char):
            if self.peek_character() == "=":
                self._read_character()
                token = Token(TokenType.GTE, ">=")
            else:
                token = Token(TokenType.GT, self.current_char)
        elif match(r'^<$', self.current_char):
            if self.peek_character() == "=":
                self._read_character()
                token = Token(TokenType.LTE, "<=")
            else:
                token = Token(TokenType.LT, self.current_char)
        elif match(r'^!$', self.current_char):
            if self.peek_character() == "=":
                self._read_character()
                token = Token(TokenType.NOE_, "!=")
            else:
                token = Token(TokenType.NOT, self.current_char)
        elif self.is_letter(self.current_char):
            literal = self._read_identifier()
            token_type = lookup_token_type(literal)
            return Token(token_type, literal)
        elif self.is_number(self.current_char):
            literal = self._read_number()
            return Token(TokenType.INT, literal)
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
            if self._peek_character() == "=":
                self._read_char()
                token = Token(TokenType.LESSERQ_THAN, "<=")
            else:
                token = Token(TokenType.LESS_THAN, self.current_char)
        elif match(r'^>$', self.current_char):
            if self._peek_character() == "=":
                self._read_char()
                token = Token(TokenType.MOREQ_THAN, ">=")
            else:
                token = Token(TokenType.GREATER_THAN, self.current_char)
        elif match(r'^\[$', self.current_char):
            token = Token(TokenType.L_BRACKET, self.current_char)
        elif match(r'^\]$', self.current_char):
            token = Token(TokenType.R_BRACKET, self.current_char)
        elif match(r'^!$', self.current_char):
            if self._peek_character() == "=":
                self._read_char()
                token = Token(TokenType.NOT_EQ, "!=")
            else:
                token = Token(TokenType.NOT, self.current_char)
        else:
            token = Token(TokenType.ILLEGAL, self.current_char)
        self._read_character()
        return token


