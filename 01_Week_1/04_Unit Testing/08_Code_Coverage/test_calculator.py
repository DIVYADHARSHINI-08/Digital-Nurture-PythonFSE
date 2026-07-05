import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 5), 10)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(5, 5), 25)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)


if __name__ == "__main__":
    unittest.main()