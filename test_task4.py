import unittest
from my_functions import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome_lowercase(self):
        self.assertTrue(is_palindrome("level"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("apple"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_case_insensitive(self):
        self.assertTrue(is_palindrome("RaceCar"))


if __name__ == '__main__':
    unittest.main()