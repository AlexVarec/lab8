import unittest 
from my_functions import is_even

class TestIsEven(unittest.TestCase):
    def test_even_positive(self):
        self.assertTrue(is_even(2))

    def test_odd_positive(self):
        self.assertFalse(is_even(7))

    def test_zero(self):
        self.assertTrue(is_even(0))

    def test_even_negative(self):
        self.assertTrue(is_even(-2))

    def test_odd_negative(self):
        self.assertFalse(is_even(-7))

    if __name__ == '__main__':
        unittest.main()


