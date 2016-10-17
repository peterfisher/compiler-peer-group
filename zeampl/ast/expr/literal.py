from .expr import Expression, Range
from typing import List


class Literal(Expression):
    pass


class IntLiteral(Literal):
    def __init__(self, r: Range, value: int):
        super().__init__(r)
        self._value = value

    @property
    def value(self) -> int:
        return self._value


class BoolLiteral(Literal):
    def __init__(self, r: Range, value: bool):
        super().__init__(r)
        self._value = value

    @property
    def value(self) -> bool:
        return self._value


class StringLiteral(Literal):
    def __init__(self, r: Range, value: str):
        super().__init__(r)
        self._value = value

    @property
    def value(self) -> str:
        return self._value


class TupleLiteral(Literal):
    def __init__(self, r: Range, expressions: List[Expression]):
        super().__init__(r)
        self._expressions = expressions


class ListLiteral(Literal):
    def __init__(self, r: Range, expressions: List[Expression]):
        super().__init__(r)
        self._expressions = expressions
