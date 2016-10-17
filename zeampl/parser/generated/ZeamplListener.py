# Generated from /Users/npohilets/compiler-peer-group/zeampl/parser/Zeampl.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZeamplParser import ZeamplParser
else:
    from ZeamplParser import ZeamplParser

# This class defines a complete listener for a parse tree produced by ZeamplParser.
class ZeamplListener(ParseTreeListener):

    # Enter a parse tree produced by ZeamplParser#module.
    def enterModule(self, ctx:ZeamplParser.ModuleContext):
        pass

    # Exit a parse tree produced by ZeamplParser#module.
    def exitModule(self, ctx:ZeamplParser.ModuleContext):
        pass


    # Enter a parse tree produced by ZeamplParser#decl.
    def enterDecl(self, ctx:ZeamplParser.DeclContext):
        pass

    # Exit a parse tree produced by ZeamplParser#decl.
    def exitDecl(self, ctx:ZeamplParser.DeclContext):
        pass


    # Enter a parse tree produced by ZeamplParser#var_decl.
    def enterVar_decl(self, ctx:ZeamplParser.Var_declContext):
        pass

    # Exit a parse tree produced by ZeamplParser#var_decl.
    def exitVar_decl(self, ctx:ZeamplParser.Var_declContext):
        pass


    # Enter a parse tree produced by ZeamplParser#func_decl.
    def enterFunc_decl(self, ctx:ZeamplParser.Func_declContext):
        pass

    # Exit a parse tree produced by ZeamplParser#func_decl.
    def exitFunc_decl(self, ctx:ZeamplParser.Func_declContext):
        pass


    # Enter a parse tree produced by ZeamplParser#arg_list.
    def enterArg_list(self, ctx:ZeamplParser.Arg_listContext):
        pass

    # Exit a parse tree produced by ZeamplParser#arg_list.
    def exitArg_list(self, ctx:ZeamplParser.Arg_listContext):
        pass


    # Enter a parse tree produced by ZeamplParser#arg.
    def enterArg(self, ctx:ZeamplParser.ArgContext):
        pass

    # Exit a parse tree produced by ZeamplParser#arg.
    def exitArg(self, ctx:ZeamplParser.ArgContext):
        pass


    # Enter a parse tree produced by ZeamplParser#type_decl.
    def enterType_decl(self, ctx:ZeamplParser.Type_declContext):
        pass

    # Exit a parse tree produced by ZeamplParser#type_decl.
    def exitType_decl(self, ctx:ZeamplParser.Type_declContext):
        pass


    # Enter a parse tree produced by ZeamplParser#class_decl.
    def enterClass_decl(self, ctx:ZeamplParser.Class_declContext):
        pass

    # Exit a parse tree produced by ZeamplParser#class_decl.
    def exitClass_decl(self, ctx:ZeamplParser.Class_declContext):
        pass


    # Enter a parse tree produced by ZeamplParser#type_expr.
    def enterType_expr(self, ctx:ZeamplParser.Type_exprContext):
        pass

    # Exit a parse tree produced by ZeamplParser#type_expr.
    def exitType_expr(self, ctx:ZeamplParser.Type_exprContext):
        pass


    # Enter a parse tree produced by ZeamplParser#list_type.
    def enterList_type(self, ctx:ZeamplParser.List_typeContext):
        pass

    # Exit a parse tree produced by ZeamplParser#list_type.
    def exitList_type(self, ctx:ZeamplParser.List_typeContext):
        pass


    # Enter a parse tree produced by ZeamplParser#tuple_type.
    def enterTuple_type(self, ctx:ZeamplParser.Tuple_typeContext):
        pass

    # Exit a parse tree produced by ZeamplParser#tuple_type.
    def exitTuple_type(self, ctx:ZeamplParser.Tuple_typeContext):
        pass


    # Enter a parse tree produced by ZeamplParser#statement.
    def enterStatement(self, ctx:ZeamplParser.StatementContext):
        pass

    # Exit a parse tree produced by ZeamplParser#statement.
    def exitStatement(self, ctx:ZeamplParser.StatementContext):
        pass


    # Enter a parse tree produced by ZeamplParser#block.
    def enterBlock(self, ctx:ZeamplParser.BlockContext):
        pass

    # Exit a parse tree produced by ZeamplParser#block.
    def exitBlock(self, ctx:ZeamplParser.BlockContext):
        pass


    # Enter a parse tree produced by ZeamplParser#expr_stmt.
    def enterExpr_stmt(self, ctx:ZeamplParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by ZeamplParser#expr_stmt.
    def exitExpr_stmt(self, ctx:ZeamplParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by ZeamplParser#assign_op.
    def enterAssign_op(self, ctx:ZeamplParser.Assign_opContext):
        pass

    # Exit a parse tree produced by ZeamplParser#assign_op.
    def exitAssign_op(self, ctx:ZeamplParser.Assign_opContext):
        pass


    # Enter a parse tree produced by ZeamplParser#if_stmt.
    def enterIf_stmt(self, ctx:ZeamplParser.If_stmtContext):
        pass

    # Exit a parse tree produced by ZeamplParser#if_stmt.
    def exitIf_stmt(self, ctx:ZeamplParser.If_stmtContext):
        pass


    # Enter a parse tree produced by ZeamplParser#while_stmt.
    def enterWhile_stmt(self, ctx:ZeamplParser.While_stmtContext):
        pass

    # Exit a parse tree produced by ZeamplParser#while_stmt.
    def exitWhile_stmt(self, ctx:ZeamplParser.While_stmtContext):
        pass


    # Enter a parse tree produced by ZeamplParser#for_stmt.
    def enterFor_stmt(self, ctx:ZeamplParser.For_stmtContext):
        pass

    # Exit a parse tree produced by ZeamplParser#for_stmt.
    def exitFor_stmt(self, ctx:ZeamplParser.For_stmtContext):
        pass


    # Enter a parse tree produced by ZeamplParser#return_stmt.
    def enterReturn_stmt(self, ctx:ZeamplParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by ZeamplParser#return_stmt.
    def exitReturn_stmt(self, ctx:ZeamplParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by ZeamplParser#break_stmt.
    def enterBreak_stmt(self, ctx:ZeamplParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by ZeamplParser#break_stmt.
    def exitBreak_stmt(self, ctx:ZeamplParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by ZeamplParser#continue_stmt.
    def enterContinue_stmt(self, ctx:ZeamplParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by ZeamplParser#continue_stmt.
    def exitContinue_stmt(self, ctx:ZeamplParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by ZeamplParser#expr.
    def enterExpr(self, ctx:ZeamplParser.ExprContext):
        pass

    # Exit a parse tree produced by ZeamplParser#expr.
    def exitExpr(self, ctx:ZeamplParser.ExprContext):
        pass


    # Enter a parse tree produced by ZeamplParser#expr5.
    def enterExpr5(self, ctx:ZeamplParser.Expr5Context):
        pass

    # Exit a parse tree produced by ZeamplParser#expr5.
    def exitExpr5(self, ctx:ZeamplParser.Expr5Context):
        pass


    # Enter a parse tree produced by ZeamplParser#expr5op.
    def enterExpr5op(self, ctx:ZeamplParser.Expr5opContext):
        pass

    # Exit a parse tree produced by ZeamplParser#expr5op.
    def exitExpr5op(self, ctx:ZeamplParser.Expr5opContext):
        pass


    # Enter a parse tree produced by ZeamplParser#expr4.
    def enterExpr4(self, ctx:ZeamplParser.Expr4Context):
        pass

    # Exit a parse tree produced by ZeamplParser#expr4.
    def exitExpr4(self, ctx:ZeamplParser.Expr4Context):
        pass


    # Enter a parse tree produced by ZeamplParser#expr4op.
    def enterExpr4op(self, ctx:ZeamplParser.Expr4opContext):
        pass

    # Exit a parse tree produced by ZeamplParser#expr4op.
    def exitExpr4op(self, ctx:ZeamplParser.Expr4opContext):
        pass


    # Enter a parse tree produced by ZeamplParser#expr3.
    def enterExpr3(self, ctx:ZeamplParser.Expr3Context):
        pass

    # Exit a parse tree produced by ZeamplParser#expr3.
    def exitExpr3(self, ctx:ZeamplParser.Expr3Context):
        pass


    # Enter a parse tree produced by ZeamplParser#expr3op.
    def enterExpr3op(self, ctx:ZeamplParser.Expr3opContext):
        pass

    # Exit a parse tree produced by ZeamplParser#expr3op.
    def exitExpr3op(self, ctx:ZeamplParser.Expr3opContext):
        pass


    # Enter a parse tree produced by ZeamplParser#expr2.
    def enterExpr2(self, ctx:ZeamplParser.Expr2Context):
        pass

    # Exit a parse tree produced by ZeamplParser#expr2.
    def exitExpr2(self, ctx:ZeamplParser.Expr2Context):
        pass


    # Enter a parse tree produced by ZeamplParser#expr2op.
    def enterExpr2op(self, ctx:ZeamplParser.Expr2opContext):
        pass

    # Exit a parse tree produced by ZeamplParser#expr2op.
    def exitExpr2op(self, ctx:ZeamplParser.Expr2opContext):
        pass


    # Enter a parse tree produced by ZeamplParser#expr1.
    def enterExpr1(self, ctx:ZeamplParser.Expr1Context):
        pass

    # Exit a parse tree produced by ZeamplParser#expr1.
    def exitExpr1(self, ctx:ZeamplParser.Expr1Context):
        pass


    # Enter a parse tree produced by ZeamplParser#expr0.
    def enterExpr0(self, ctx:ZeamplParser.Expr0Context):
        pass

    # Exit a parse tree produced by ZeamplParser#expr0.
    def exitExpr0(self, ctx:ZeamplParser.Expr0Context):
        pass


    # Enter a parse tree produced by ZeamplParser#literal.
    def enterLiteral(self, ctx:ZeamplParser.LiteralContext):
        pass

    # Exit a parse tree produced by ZeamplParser#literal.
    def exitLiteral(self, ctx:ZeamplParser.LiteralContext):
        pass


    # Enter a parse tree produced by ZeamplParser#tuple_literal.
    def enterTuple_literal(self, ctx:ZeamplParser.Tuple_literalContext):
        pass

    # Exit a parse tree produced by ZeamplParser#tuple_literal.
    def exitTuple_literal(self, ctx:ZeamplParser.Tuple_literalContext):
        pass


    # Enter a parse tree produced by ZeamplParser#list_literal.
    def enterList_literal(self, ctx:ZeamplParser.List_literalContext):
        pass

    # Exit a parse tree produced by ZeamplParser#list_literal.
    def exitList_literal(self, ctx:ZeamplParser.List_literalContext):
        pass


