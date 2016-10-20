
_escape_chars = {
    'a': '\a',
    'b': '\b',
    'f': '\f',
    'n': '\n',
    'r': '\r',
    't': '\t',
    'v': '\v',
}

def unescape_string(s):
    if len(s) > 0 and s[0] == '\"':
        s = s[1:]
    if len(s) > 0 and s[-1] == '\"':
        s = s[:-1]
    state = 0
    r = ''  # result accumulator
    x = 0  # hex digits accumulator
    x_fallback = ''
    for c in s:
        if state == 0:  # default
            if c == '\\':
                state = -1
            else:
                r += c
        elif state == -1:  # after slash
            if c in '\\\'\"':
                r += c
                state = 0
            elif c == 'x':
                state = 2
                x_fallback = '\\x'
            elif c == 'u':
                state = 4
                x_fallback = '\\u'
            elif c == 'U':
                state = 8
                x_fallback = '\\U'
            else:
                r += _escape_chars.get(c, '\\' + c)
                state = 0
        else:
            append_c = False
            try:
                x = x * 16 + int(c, 16)
                state -= 1
                x_fallback = ''
            except ValueError:
                append_c = True
                state = 0
            if state == 0:
                if len(x_fallback) > 0:
                    r += x_fallback
                else:
                    r += chr(x)
                x = 0
                if append_c:
                    r += c

    if state == 0:
        pass
    elif state == -1:
        r += '\\'
    else:
        if len(x_fallback) > 0:
            r += x_fallback
        else:
            r += chr(x)
    return r
