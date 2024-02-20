from Lang.token import (
    Token, TokenType
)
from Lang.lexer import Lexer


def start_repl():
    print("Welcome to the Monkey programming language")
    while (source := input(">>>")) != "exit":
        lexer = Lexer(source)
        while (token := lexer.next_token()) != Token(TokenType.EOF, ""):
            print(token)
