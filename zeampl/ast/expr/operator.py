from .expr import Expression, Range


class PrefixOperatorExpression(Expression):
    def __init__(self, r: Range, op: str, expr: Expression):
        super().__init__(r)
        self._op = op
        self._expr = expr

    @property
    def op(self) -> str:
        return self._op

    @property
    def expr(self):
        return self._expr


class BinaryOperatorExpression(Expression):
    def __init__(self, r: Range, lhs: Expression, op: str, rhs: Expression):
        super().__init__(r)
        self._lhs = lhs
        self._op = op
        self._rhs = rhs

    @property
    def lhs(self) -> Expression:
        return self._lhs

    @property
    def op(self) -> str:
        return self._op

    @property
    def rhs(self) -> Expression:
        return self._rhs
