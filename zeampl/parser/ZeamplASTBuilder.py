from .generated import ZeamplParser
from .generated import ZeamplVisitor
import antlr4
import ast
from parser.string_utils import unescape_string


class ZeamplASTBuilder(ZeamplVisitor):
    def __init__(self, token_stream: antlr4.CommonTokenStream):
        self._token_stream = token_stream

    def get_range(self, ctx: antlr4.ParserRuleContext) -> ast.Range:
        start_tok = ctx.start  # type: antlr4.Token
        end_tok = self._token_stream.get(ctx.stop.tokenIndex + 1)  # type: antlr4.Token
        file_name = start_tok.getInputStream().name
        return ast.Range(file_name, start_tok.line, start_tok.column + 1, end_tok.line, end_tok.column + 1)

    def visitIntLiteral(self, ctx: ZeamplParser.IntLiteralContext):
        value = int(ctx.getText())
        return ast.IntLiteral(self.get_range(ctx), value)

    def visitBoolLiteral(self, ctx: ZeamplParser.BoolLiteralContext):
        value = {'true': True, 'false': False}[ctx.getText()]
        return ast.BoolLiteral(self.get_range(ctx), value)

    def visitStringLiteral(self, ctx: ZeamplParser.StringLiteralContext):
        value = unescape_string(ctx.getText())
        return ast.StringLiteral(self.get_range(ctx), value)

