# Generated from /Users/npohilets/compiler-peer-group/zeampl/parser/Zeampl.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZeamplParser import ZeamplParser
else:
    from ZeamplParser import ZeamplParser

# This class defines a complete generic visitor for a parse tree produced by ZeamplParser.

class ZeamplVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZeamplParser#module.
    def visitModule(self, ctx:ZeamplParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#decl.
    def visitDecl(self, ctx:ZeamplParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#varDecl.
    def visitVarDecl(self, ctx:ZeamplParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#funcDecl.
    def visitFuncDecl(self, ctx:ZeamplParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#argList.
    def visitArgList(self, ctx:ZeamplParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#arg.
    def visitArg(self, ctx:ZeamplParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#typeDecl.
    def visitTypeDecl(self, ctx:ZeamplParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#classDecl.
    def visitClassDecl(self, ctx:ZeamplParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#type_expr.
    def visitType_expr(self, ctx:ZeamplParser.Type_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#list_type.
    def visitList_type(self, ctx:ZeamplParser.List_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#tuple_type.
    def visitTuple_type(self, ctx:ZeamplParser.Tuple_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#statement.
    def visitStatement(self, ctx:ZeamplParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#block.
    def visitBlock(self, ctx:ZeamplParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#exprStmt.
    def visitExprStmt(self, ctx:ZeamplParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#assign_op.
    def visitAssign_op(self, ctx:ZeamplParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#ifStmt.
    def visitIfStmt(self, ctx:ZeamplParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#whileStmt.
    def visitWhileStmt(self, ctx:ZeamplParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#forStmt.
    def visitForStmt(self, ctx:ZeamplParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#returnStmt.
    def visitReturnStmt(self, ctx:ZeamplParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#breakStmt.
    def visitBreakStmt(self, ctx:ZeamplParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#continueStmt.
    def visitContinueStmt(self, ctx:ZeamplParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#expr.
    def visitExpr(self, ctx:ZeamplParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#expr5.
    def visitExpr5(self, ctx:ZeamplParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#expr5op.
    def visitExpr5op(self, ctx:ZeamplParser.Expr5opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#expr4.
    def visitExpr4(self, ctx:ZeamplParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#expr4op.
    def visitExpr4op(self, ctx:ZeamplParser.Expr4opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#expr3.
    def visitExpr3(self, ctx:ZeamplParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#expr3op.
    def visitExpr3op(self, ctx:ZeamplParser.Expr3opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#expr2.
    def visitExpr2(self, ctx:ZeamplParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#expr2op.
    def visitExpr2op(self, ctx:ZeamplParser.Expr2opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#expr1.
    def visitExpr1(self, ctx:ZeamplParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#expr0.
    def visitExpr0(self, ctx:ZeamplParser.Expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#literal.
    def visitLiteral(self, ctx:ZeamplParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#intLiteral.
    def visitIntLiteral(self, ctx:ZeamplParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#boolLiteral.
    def visitBoolLiteral(self, ctx:ZeamplParser.BoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#stringLiteral.
    def visitStringLiteral(self, ctx:ZeamplParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#tupleLiteral.
    def visitTupleLiteral(self, ctx:ZeamplParser.TupleLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#listLiteral.
    def visitListLiteral(self, ctx:ZeamplParser.ListLiteralContext):
        return self.visitChildren(ctx)



del ZeamplParser