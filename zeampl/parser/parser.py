from antlr4 import InputStream
from antlr4.BufferedTokenStream import BufferedTokenStream
from .generated import ZeamplLexer, ZeamplParser
from .ZeamplASTBuilder import ZeamplASTBuilder


def parse_literal(s: str):
    input = InputStream(s)
    lex = ZeamplLexer(input)
    tok_stream = BufferedTokenStream(lex)
    p = ZeamplParser(tok_stream)
    ctx = p.literal()
    builder = ZeamplASTBuilder(tok_stream)
    return ctx.accept(builder)
