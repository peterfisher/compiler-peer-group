from ..range import Range


class Expression(object):
    def __init__(self, r: Range):
        self._range = r

    @property
    def range(self) -> Range:
        return self._range

