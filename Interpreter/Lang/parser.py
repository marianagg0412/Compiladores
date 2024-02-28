from enum import IntEnum
from typing import (
    Callable,
    Dict,
    List,
    Optional
)
from Lang.lexer import Lexer
from Lang.token import (
    Token,
    TokenType
)
from Lang.ast import Program


class Precedence(IntEnum):
    LOWEST = 1
    EQUALS = 2
    LESSGREATER = 3
    SUM = 4
    PRODUCT = 5
    PREFIX = 6
    CALL = 7


PRECEDENCES: Dict[TokenType, Precedence] = {  # Tiene todos los elementos
    TokenType.EQ: Precedence.EQUALS,
    TokenType.NOE: Precedence.EQUALS,
    TokenType.LT: Precedence.LESSGREATER,
    TokenType.GT: Precedence.LESSGREATER,
    TokenType.PLUS: Precedence.SUM,
    TokenType.MINUS: Precedence.SUM,
    TokenType.DIV: Precedence.PRODUCT,
    TokenType.MULTIPLICATION: Precedence.PRODUCT,
    TokenType.L_PAREN: Precedence.CALL,
}


class Parser:
    def __init__(self, lexer: Lexer) -> None:
        self.lexer = lexer
        self.current_token: Optional[Token] = None
        self.peek_token: Optional[Token] = None
        self.errors: List[str] = []

        self._advance_tokens()
        self._advance_tokens()

    def _advance_tokens(self) -> None:
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_program(self) -> Program:
        program: Program = Program(statements=[])
        while self.current_token.token_type != TokenType.EOF:
            print(self.current_token)
            self._advance_tokens()
        return program