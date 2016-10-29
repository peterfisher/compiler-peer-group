from antlr4 import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from .generated import ZeamplLexer, ZeamplParser
from .ZeamplASTBuilder import ZeamplASTBuilder
import ast
from typing import Optional


def parse(s, method):
    input = InputStream(s)
    lex = ZeamplLexer(input)
    tok_stream = CommonTokenStream(lex)
    p = ZeamplParser(tok_stream)
    ctx = method(p)
    builder = ZeamplASTBuilder(tok_stream)
    return ctx.accept(builder)


def parse_literal(s: str) -> Optional[ast.Literal]:
    return parse(s, ZeamplParser.literal)


def parse_expression(s: str) -> Optional[ast.Expression]:
    return parse(s, ZeamplParser.expr)


