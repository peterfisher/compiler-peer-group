from .generated import ZeamplParser
from .generated import ZeamplVisitor
import antlr4
import ast


class ZeamplASTBuilder(ZeamplVisitor):
    def __init__(self, token_stream: antlr4.CommonTokenStream):
        self._token_stream = token_stream

    def get_range(self, ctx: antlr4.ParserRuleContext) -> ast.Range:
        start_tok = ctx.start  # type: antlr4.Token
        end_tok = self._token_stream.get(ctx.stop.tokenIndex + 1)  # type: antlr4.Token
        file_name = start_tok.getInputStream().name
        return ast.Range(file_name, start_tok.line, start_tok.column + 1, end_tok.line, end_tok.column + 1)

    def visitIntLiteral(self, ctx:ZeamplParser.IntLiteralContext):
        return ast.IntLiteral(self.get_range(ctx), int(ctx.getText()))


