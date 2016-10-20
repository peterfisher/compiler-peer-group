from .generated import ZeamplParser
from .generated import ZeamplVisitor
import antlr4
import ast
from parser.string_utils import unescape_string
from typing import List


class ZeamplASTBuilder(ZeamplVisitor):
    def __init__(self, token_stream: antlr4.BufferedTokenStream):
        self._token_stream = token_stream

    def get_range(self, ctx: antlr4.ParserRuleContext) -> ast.Range:
        start_tok = ctx.start  # type: antlr4.Token
        end_tok = self._token_stream.get(ctx.stop.tokenIndex + 1)  # type: antlr4.Token
        file_name = start_tok.getInputStream().name
        return ast.Range(file_name, start_tok.line, start_tok.column + 1, end_tok.line, end_tok.column + 1)

    def get_expressions(self, contexts: List[antlr4.ParserRuleContext]):
        return [ctx.accept(self) for ctx in contexts]

    def visitIntLiteral(self, ctx: ZeamplParser.IntLiteralContext):
        value = int(ctx.getText())
        return ast.IntLiteral(self.get_range(ctx), value)

    def visitBoolLiteral(self, ctx: ZeamplParser.BoolLiteralContext):
        value = {'true': True, 'false': False}[ctx.getText()]
        return ast.BoolLiteral(self.get_range(ctx), value)

    def visitStringLiteral(self, ctx: ZeamplParser.StringLiteralContext):
        value = unescape_string(ctx.getText())
        return ast.StringLiteral(self.get_range(ctx), value)

    def visitTupleLiteral(self, ctx: ZeamplParser.TupleLiteralContext):
        return ast.TupleLiteral(self.get_range(ctx), self.get_expressions(ctx.x))

    def visitListLiteral(self, ctx: ZeamplParser.ListLiteralContext):
        return ast.ListLiteral(self.get_range(ctx), self.get_expressions(ctx.x))

    def visitIdentifierExpression(self, ctx: ZeamplParser.IdentifierExpressionContext):
        token = ctx.ID().symbol  # type: antlr4.Token
        return ast.IdentifierExpression(self.get_range(ctx), token.text)
