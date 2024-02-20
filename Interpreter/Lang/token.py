from enum import (
    Enum, auto, unique
)

from typing import (
    Dict, NamedTuple
)

"""
Class TokenType to define token types
Each token type is a unique value and its identifier is a string and it does not repeat
"""


@unique
class TokenType(Enum):
    ASSIGN = auto() #=
    PLUS = auto() #+
    COMMA = auto() #,
    ILLEGAL = auto() #?±
    SEMICOLON = auto() #;
    EOF = auto() #End of file
    L_PAREN = auto() #(
    R_PAREN = auto() #)
    L_BRACE = auto() #{
    R_BRACE = auto() #}
    MINUS = auto() #-
    DIVISION = auto() #/
    MULTIPLICATION = auto() #*
    LESS_THAN = auto() #<
    GREATER_THAN = auto() #>
    L_BRACKET = auto() #[
    R_BRACKET = auto() #]
    NOT = auto() #!


class Token(NamedTuple):
    type: TokenType
    value: str

    def __str__(self) -> str:
        return f'{self.type.name} : {self.value}'



