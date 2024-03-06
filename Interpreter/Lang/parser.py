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
from Lang.ast import (
    Program,
    Statement,
    ExpressionStatement,
    Expression, Infix, Prefix
)

PrefixParseFn = Callable[[], Optional[Expression]]
InfixParseFn = Callable[[Expression], Optional[Expression]]
PrefixParseFns = Dict[TokenType, PrefixParseFn]
InfixParseFns = Dict[TokenType, InfixParseFn]


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
        self._lexer = lexer  # Make all attributes private in dart
        self._current_token: Optional[Token] = None
        self._peek_token: Optional[Token] = None
        self._errors: List[str] = []
        self._prefix_parse_fns: PrefixParseFns = self._register_prefix_fns()
        self._infix_parse_fns: InfixParseFns = self._register_infix_fns()

        self._advance_tokens()
        self._advance_tokens()

    def _advance_tokens(self) -> None:
        self._current_token = self._peek_token
        self._peek_token = self._lexer.next_token()

    def parse_program(self) -> Program:
        program: Program = Program(statements=[])
        while self._current_token.token_type != TokenType.EOF:
            print(self._current_token)
            self._advance_tokens()
        return program

    def _parse_statement(self) -> Optional[Statement]:
        assert self._current_token is not None
        if self._current_token.token_type == TokenType.LET:
            # Todo: Parse let statement
            pass
        elif self._current_token.token_type == TokenType.RETURN:
            pass
        return self._parse_expression_statement()

    def _parse_expression_statement(self) -> Optional[ExpressionStatement]:
        pass

    def _parse_expression(self, precedence: Precedence) -> Optional[Expression]:
        assert self._current_token is not None
        try:
            prefix = self._prefix_parse_fns[self._current_token.token_type]
        except KeyError:
            print("No se puede parsear la expresion")
            return None

    """
    We create the infix_expression function to split the data.
    It has a left expression and to the right, it may or not have an expression
    """

    def _register_infix_fns(self) -> InfixParseFns:
        return {
            TokenType.PLUS: self._parse_infix_expression,
            TokenType.MINUS: self._parse_infix_expression,
            TokenType.MULTIPLICATION: self._parse_infix_expression,
            TokenType.DIV: self._parse_infix_expression,
            TokenType.EQ: self._parse_infix_expression,
            TokenType.NOE: self._parse_infix_expression,
            TokenType.LT: self._parse_infix_expression,
            TokenType.GT: self._parse_infix_expression,
            TokenType.L_PAREN: self._parse_infix_expression,
            TokenType.R_PAREN: self._parse_infix_expression,
        }

    def _parse_infix_expression(self, left: Expression) -> Optional[Expression]:
        assert self._current_token is not None
        infix = Infix(token=self._current_token, operator=self._current_token.literal, left=left)
        precedence = self.current_precedence()
        self._advance_tokens()
        infix.right = self._parse_expression(precedence)
        return infix

    """
    _current_precedence() returns the priority of the operator to be evaluated by the parser
    """

    def current_precedence(self) -> Precedence:
        assert self._current_token is not None
        try:
            return PRECEDENCES[self._current_token.token_type]
        except KeyError:
            return Precedence.LOWEST

    def _register_prefix_fns(self) -> PrefixParseFns:
        return {
            TokenType.MINUS: self._parse_prefix_expression,
            TokenType.NOT: self._parse_prefix_expression,
        }

    def _parse_prefix_expression(self) -> Optional[Expression]:
        assert self._current_token is not None
        prefix_expression = Prefix(token=self._current_token,
                                   operator=self._current_token.literal)
        self._advance_tokens()
        prefix_expression.right = self._parse_expression(Precedence.PREFIX)

        return prefix_expression

