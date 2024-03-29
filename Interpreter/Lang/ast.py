from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    List,
    Optional
)
from Lang.token import Token


class ASTNode(ABC):
    @abstractmethod
    def token_literal(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Statement(ASTNode):
    def __init__(self, token: Token) -> None:
        self.token = token

    def token_literal(self) -> str:
        return self.token.literal


class Expression(ASTNode):
    def __init__(self, token: Token) -> None:
        self.token = token

    def token_literal(self) -> str:
        return self.token.literal


class Program(ASTNode):
    def __init__(self, statements: List[Statement]) -> None:
        self.statements = statements

    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        return ''

    def __str__(self) -> str:
        out: List[str] = []
        for statement in self.statements:
            out.append(str(statement))
        # Vuelve una lista en un string
        return ''.join(out)


class Identifier(Expression):
    def __init__(self, token: Token, value: str) -> None:
        super().__init__(token)
        self.value = value

    def __str__(self) -> str:
        return self.value


class LetStatement(Statement):
    def __init__(self, token: Token, name: Identifier, value: Optional[Expression] = None) -> None:
        super().__init__(token)
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f'{self.token_literal()} {self.name} = {self.value}'


class ReturnStatement(Statement):
    def __init__(self, token: Token, value: Optional[Expression]) -> None:
        super().__init__(token)
        self.return_value = value

    def __str__(self) -> str:
        return f'{self.token_literal()} {str(self.return_value)}'


class ExpressionStatement(Statement):
    def __init__(self, token: Token, expression: Optional[Expression]) -> None:
        super().__init__(token)
        self.expression = expression

    def __str__(self) -> str:
        return str(self.expression)


class IntegerLiteral(Expression):
    def __init__(self, token: Token, value: Optional[int]) -> None:
        super().__init__(token)
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Prefix(Expression):
    def __init__(self, token: Token, operator: str, right: Optional[Expression] = None) -> None:
        super().__init__(token)
        self.operator = operator
        self.right = right

    def __str__(self) -> str:
        return f'{self.operator}{str(self.right)}'


class Infix(Expression):
    def __init__(self, token: Token, left: Expression, operator: str, right: Optional[Expression] = None) -> None:
        super().__init__(token)
        self.operator = operator
        self.left = left
        self.right = right

    def __str__(self):
        return f'({str(self.left)} {self.operator} {str(self.right)})'


class Boolean(Expression):
    def __init__(self, token: Token, value: Optional[bool] = None) -> None:
        super().__init__(token)
        self.value = value

    def __str__(self) -> str:
        return self.token_literal()
