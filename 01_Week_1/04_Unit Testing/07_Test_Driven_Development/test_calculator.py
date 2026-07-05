import unittest
from calculator import add


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 10), 15)

    def test_add_negative(self):
        self.assertEqual(add(-5, 5), 0)


if __name__ == "__main__":
    unittest.main()