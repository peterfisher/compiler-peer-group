""" Provides for AST construction for funcs and methods calls
"""

from .expr import Expression, Range


class FuncExpression(Expression):
    """ Expression Token Type: expr1

    """
    def __init__(self, r: Range, ID, name):
        super().__init__(r)
        self._funcName = name
        self._ID = ID

    @property
    def name(self):
        return self._funcName

    @property
    def ID(self):
        return self._ID

