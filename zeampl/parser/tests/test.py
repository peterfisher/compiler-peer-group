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
