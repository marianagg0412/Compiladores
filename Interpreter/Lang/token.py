from enum import (
    Enum,
    auto,
    unique

)
from typing import (
    Dict,
    NamedTuple
)

"""
Se crea una clase TokenType que contiene los tipos de tokens 
Cada token es único y su identificador no se repite
"""


@unique
class TokenType(Enum):
    ASSIGN = auto()  # =
    COMMA = auto()  # ,
    DOT = auto()  # .
    DIV = auto()  # /
    FALSE = auto()  # false
    TRUE = auto()  # true
    IF = auto()  # if
    ELSE = auto()  # else
    FUNCTION = auto()  # function
    RETURN = auto()  # return
    EOF = auto()  # nada
    EQ = auto()  # =
    GT = auto()  # >
    GTE = auto()  # >=
    IDENT = auto()  # identificador
    LET = auto()  # let
    ILLEGAL = auto()  # ?
    INT = auto()  # entero
    LT = auto()  # <
    LTE = auto()  # <=
    NOE_ = auto()  # !=
    NOT = auto()  # !
    PLUS = auto()  # +
    SEMICOLON = auto()  # ;
    L_PAREN = auto()  # (
    R_PAREN = auto()  # )
    L_BRACE = auto()  # {
    R_BRACE = auto()  # }
    MINUS = auto()  # -
    DIVISION = auto()  # /
    MULTIPLICATION = auto()  # *
    LESS_THAN = auto()  # <
    GREATER_THAN = auto()  # >
    L_BRACKET = auto()  # [
    R_BRACKET = auto()  # ]
    """
    {,},[,],+,/,(,)^,!,<,>
    """


class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'{self.token_type.name}:{self.literal}'


def lookup_token_type(token_type: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'false': TokenType.FALSE,
        'true': TokenType.TRUE,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'let': TokenType.LET,
        'function': TokenType.FUNCTION,
        'return': TokenType.RETURN,
        'EOF': TokenType.EOF,
        'ident': TokenType.IDENT,
        'int': TokenType.INT,
    }
    return keywords.get(token_type, TokenType.IDENT)

