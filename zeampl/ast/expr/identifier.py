from .expr import Expression, Range
from ..decl.declaration import Declaration
import weakref
from typing import Optional


class IdentifierExpression(Expression):
    def __init__(self, r: Range, name: str):
        super().__init__(r)
        self._name = name
        # After name resolution this will contain weak reference to a declaration
        self._declaration = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def declaration(self) -> Optional[Declaration]:
        if self._declaration is None:
            return None
        else:
            return self._declaration()

    @declaration.setter
    def declaration(self, declaration: Optional[Declaration]):
        if decl is None:
            self._declaration = None
        else:
            self._declaration = weakref.ref(declaration)
