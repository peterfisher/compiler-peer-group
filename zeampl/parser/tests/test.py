import unittest
import ast
import parser


class TestParser(unittest.TestCase):
    def test_literal_parsing(self):
        x = parser.parse_literal('123')
        self.assertIsInstance(x, ast.IntLiteral)
        self.assertEqual(x.range, ast.Range('<empty>', 1, 1, 1, 4))
        self.assertEqual(x.value, 123)
