from abc import (
    ABC,
    abstractmethod
)

from enum import (
    Enum,
    auto
)


class ObjectType(Enum):
    """
    Can add objects that will be used in the interpreter
    Can add any data types
    """
    BOOLEAN = auto()
    INTEGER = auto()
    NULL = auto()
    STRING = auto()


class Object(ABC):
    @abstractmethod
    def type(self) -> ObjectType:
        # We put pass given that in Python methods are required to have a body
        # Given that it is an abstract method, we don't need to implement it
        pass

    @abstractmethod
    def inspect(self) -> str:
        pass


class Integer(Object):
    def __init__(self, value: int) -> None:
        self.value = value

    def type(self) -> ObjectType:
        return ObjectType.INTEGER

    def inspect(self) -> str:
        return str(self.value)


class Boolean(Object):
    def __init__(self, value: bool) -> None:
        self.value = value

    def type(self) -> ObjectType:
        return ObjectType.BOOLEAN

    def inspect(self) -> str:
        return str(self.value)


class Null(Object):
    def type(self) -> ObjectType:
        return ObjectType.NULL

    def inspect(self) -> str:
        return 'null'


class String(Object):
    def __init__(self, value: str) -> None:
        self.value = value

    def type(self) -> ObjectType:
        return ObjectType.STRING

    def inspect(self) -> str:
        return str(self.value)

