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


    # Visit a parse tree produced by ZeamplParser#var_decl.
    def visitVar_decl(self, ctx:ZeamplParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#func_decl.
    def visitFunc_decl(self, ctx:ZeamplParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#arg_list.
    def visitArg_list(self, ctx:ZeamplParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#arg.
    def visitArg(self, ctx:ZeamplParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#type_decl.
    def visitType_decl(self, ctx:ZeamplParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#class_decl.
    def visitClass_decl(self, ctx:ZeamplParser.Class_declContext):
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


    # Visit a parse tree produced by ZeamplParser#expr_stmt.
    def visitExpr_stmt(self, ctx:ZeamplParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#assign_op.
    def visitAssign_op(self, ctx:ZeamplParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#if_stmt.
    def visitIf_stmt(self, ctx:ZeamplParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#while_stmt.
    def visitWhile_stmt(self, ctx:ZeamplParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#for_stmt.
    def visitFor_stmt(self, ctx:ZeamplParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZeamplParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZeamplParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZeamplParser.Continue_stmtContext):
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


    # Visit a parse tree produced by ZeamplParser#tuple_literal.
    def visitTuple_literal(self, ctx:ZeamplParser.Tuple_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeamplParser#list_literal.
    def visitList_literal(self, ctx:ZeamplParser.List_literalContext):
        return self.visitChildren(ctx)



del ZeamplParser