from Lang.token import (
    Token, TokenType
)
from Lang.lexer import Lexer
from Lang.parser import Parser
from Lang.ast import Program


def start_repl():
    print("Sind alles Wilkommen")
    while (source := input(">>>")) != "exit":
        lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()