import unittest
import convert

class TestCases(unittest.TestCase):

    def test_str_to_float_1(self):
        input = "1.1"
        expected = 1.1
        actual = convert.str_to_float(input)
        self.assertEqual(expected, actual)

    def test_str_to_float_2(self):
        input = "hello"
        expected = None
        actual = convert.str_to_float(input)
        self.assertEqual(expected, actual)
