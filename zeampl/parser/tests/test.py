import unittest
import ast
import parser


class TestParser(unittest.TestCase):
    def test_string_escaping(self):
        self.assertEqual(parser.unescape_string("\"\\t\\n\\v\\f\\b\""), '\t\n\v\f\b')
        self.assertEqual(parser.unescape_string("\"abc\\xDE\\xa0\\u1235\\U0001034288\""), 'abc\xDE\xA0\u1235\U00010342' + '88')
        self.assertEqual(parser.unescape_string("\"abc\\"), 'abc\\')
        self.assertEqual(parser.unescape_string("\"abc\\z"), 'abc\\z')
        self.assertEqual(parser.unescape_string("\"abc\\x"), 'abc\\x')
        self.assertEqual(parser.unescape_string("\"abc\\x1"), 'abc\x01')
        self.assertEqual(parser.unescape_string("\"abc\\x1|"), 'abc\x01|')
        self.assertEqual(parser.unescape_string("\"abc\\u"), 'abc\\u')
        self.assertEqual(parser.unescape_string("\"abc\\u1"), 'abc\x01')
        self.assertEqual(parser.unescape_string("\"abc\\u1|"), 'abc\x01|')
        self.assertEqual(parser.unescape_string("\"abc\\U"), 'abc\\U')
        self.assertEqual(parser.unescape_string("\"abc\\U1"), 'abc\x01')
        self.assertEqual(parser.unescape_string("\"abc\\U1|"), 'abc\x01|')

    def test_int_literal(self):
        x = parser.parse_literal('123')
        self.assertIsInstance(x, ast.IntLiteral)
        self.assertEqual(x.range, ast.Range('<empty>', 1, 1, 1, 4))
        self.assertEqual(x.value, 123)

    def test_bool_literal(self):
        x = parser.parse_literal('true')
        self.assertIsInstance(x, ast.BoolLiteral)
        self.assertEqual(x.range, ast.Range('<empty>', 1, 1, 1, 5))
        self.assertEqual(x.value, True)
        x = parser.parse_literal('false')
        self.assertIsInstance(x, ast.BoolLiteral)
        self.assertEqual(x.range, ast.Range('<empty>', 1, 1, 1, 6))
        self.assertEqual(x.value, False)

    def test_string_literal(self):
        x = parser.parse_literal('\"some\\ntext\"')
        self.assertIsInstance(x, ast.StringLiteral)
        self.assertEqual(x.range, ast.Range('<empty>', 1, 1, 1, 13))
        self.assertEqual(x.value, 'some\ntext')

    def test_tuple_literal(self):
        x = parser.parse_literal('(1, (true, \"abc\"), ())')
        self.assertIsInstance(x, ast.TupleLiteral)
        self.assertEqual(x.range, ast.Range('<empty>', 1, 1, 1, 23))
        self.assertEqual(len(x.expressions), 3)
        self.assertIsInstance(x.expressions[0], ast.IntLiteral)
        self.assertEqual(x.expressions[0].value, 1)
        self.assertIsInstance(x.expressions[1], ast.TupleLiteral)
        self.assertEqual(x.expressions[1].range, ast.Range('<empty>', 1, 5, 1, 18))
        self.assertEqual(len(x.expressions[1].expressions), 2)
        self.assertIsInstance(x.expressions[1].expressions[0], ast.BoolLiteral)
        self.assertEqual(x.expressions[1].expressions[0].value, True)
        self.assertIsInstance(x.expressions[1].expressions[1], ast.StringLiteral)
        self.assertEqual(x.expressions[1].expressions[1].value, 'abc')
        self.assertIsInstance(x.expressions[2], ast.TupleLiteral)
        self.assertEqual(x.expressions[2].range, ast.Range('<empty>', 1, 20, 1, 22))
        self.assertEqual(len(x.expressions[2].expressions), 0)

    def test_list_literal(self):
        x = parser.parse_literal('[1, (true, \"abc\"), ()]')
        self.assertIsInstance(x, ast.ListLiteral)
        self.assertEqual(x.range, ast.Range('<empty>', 1, 1, 1, 23))
        self.assertEqual(len(x.expressions), 3)
        self.assertIsInstance(x.expressions[0], ast.IntLiteral)
        self.assertEqual(x.expressions[0].value, 1)
        self.assertIsInstance(x.expressions[1], ast.TupleLiteral)
        self.assertEqual(x.expressions[1].range, ast.Range('<empty>', 1, 5, 1, 18))
        self.assertEqual(len(x.expressions[1].expressions), 2)
        self.assertIsInstance(x.expressions[1].expressions[0], ast.BoolLiteral)
        self.assertEqual(x.expressions[1].expressions[0].value, True)
        self.assertIsInstance(x.expressions[1].expressions[1], ast.StringLiteral)
        self.assertEqual(x.expressions[1].expressions[1].value, 'abc')
        self.assertIsInstance(x.expressions[2], ast.TupleLiteral)
        self.assertEqual(x.expressions[2].range, ast.Range('<empty>', 1, 20, 1, 22))
        self.assertEqual(len(x.expressions[2].expressions), 0)

    def test_identifier(self):
        x = parser.parse_expression('x1')
        self.assertIsInstance(x, ast.IdentifierExpression)
        self.assertEqual(x.name, 'x1')
        x = parser.parse_expression('_')
        self.assertIsInstance(x, ast.IdentifierExpression)
        self.assertEqual(x.name, '_')
        x = parser.parse_expression('Xyz')
        self.assertIsInstance(x, ast.IdentifierExpression)
        self.assertEqual(x.name, 'Xyz')

    def test_expr_priority(self):
        x = parser.parse_expression('-1 + 2 * + 3')
        self.assertIsInstance(x, ast.BinaryOperatorExpression)
        self.assertEqual(x.range, ast.Range('<empty>', 1, 1, 1, 13))
        x_lhs = x.lhs
        self.assertIsInstance(x_lhs, ast.PrefixOperatorExpression)
        self.assertEqual(x_lhs.range, ast.Range('<empty>', 1, 1, 1, 3))
        self.assertEqual(x_lhs.op, '-')
        self.assertIsInstance(x_lhs.expr, ast.IntLiteral)
        self.assertEqual(x_lhs.expr.value, 1)
        x_rhs = x.rhs
        self.assertIsInstance(x_rhs, ast.BinaryOperatorExpression)
        self.assertEqual(x_rhs.range, ast.Range('<empty>', 1, 6, 1, 13))
        x_rhs_lhs = x_rhs.lhs
        self.assertIsInstance(x_rhs_lhs, ast.IntLiteral)
        self.assertEqual(x_rhs_lhs.range, ast.Range('<empty>', 1, 6, 1, 7))
        self.assertEqual(x_rhs_lhs.value, 2)
        x_rhs_rhs = x_rhs.rhs
        self.assertIsInstance(x_rhs_rhs, ast.PrefixOperatorExpression)
        self.assertEqual(x_rhs_rhs.range, ast.Range('<empty>', 1, 10, 1, 13))
        self.assertEqual(x_rhs_rhs.op, '+')
        x_rhs_rhs_expr = x_rhs_rhs.expr
        self.assertIsInstance(x_rhs_rhs_expr, ast.IntLiteral)
        self.assertEqual(x_rhs_rhs_expr.range, ast.Range('<empty>', 1, 12, 1, 13))
        self.assertEqual(x_rhs_rhs_expr.value, 3)

    def test_function_expression(self):
        tests = [
            # Func calls
            'skittles', 'skittles(rainbox)', 'skittles(taste, rainbow)',
            # Method calls
            'rainbow.skittles', 'rainbow.skittles(taste)', 'rainbow.skittles(taste, skookum)',
        ]

        for case in tests:
            result = parser.parse_expression(case)
            self.assertIsInstance(result, ast.FuncExpression)


