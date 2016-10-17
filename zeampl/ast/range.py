class Location(object):
    def __init__(self, file: str, line: int, column: int):
        self._file = file
        self._line = line
        self._column = column

    @property
    def file(self):
        return self._file

    @property
    def line(self) -> int:
        return self._line

    @property
    def column(self) -> int:
        return self._column

    def __str__(self):
        return self._file + ':' + str(self._line) + ':' + str(self._column)

    def __repr__(self):
        x = [self._file, self._line, self._column]
        return 'Location(' + ','.join([repr(y) for y in x]) + ')'

    def __hash__(self):
        return self._line * 97 + self._column

    def __eq__(self, other):
        if isinstance(other, Location):
            return other._line == self._line and other._column == self._column and other._file == self._file
        else:
            return False


class Range(object):
    def __init__(self, file, start_line, start_column, end_line, end_column):
        self._file = file
        self._start_line = start_line
        self._start_column = start_column
        self._end_line = end_line
        self._end_column = end_column

    @property
    def start(self):
        return Location(self._file, self._start_line, self._start_column)

    @property
    def end(self):
        return Location(self._file, self._end_line, self._end_column)

    def __str__(self):
        s = str(self.start)
        s += '-'
        if self._end_line != self._start_line:
            s += str(self._end_line) + ':'
        s += str(self._end_column)
        return s

    def __repr__(self):
        x = [self._file, self._start_line, self._start_column, self._end_line, self._end_column]
        return 'Range(' + ','.join([repr(y) for y in x]) + ')'

    def __hash__(self):
        return self._start_line * 97 + self._start_column

    def __eq__(self, other):
        if isinstance(other, Range):
            return self._start_line == other._start_line and self._start_column == other._start_column \
                and self._end_line == other._end_line and self._end_column == other._end_column \
                and self._file == other._file
        else:
            return False
