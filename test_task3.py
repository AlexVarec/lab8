import unittest
from my_functions import reverse_string

class TestReverseString(unittest.TestCase):
    def test_normal_string(self):
        self.assertEqual(reverse_string("Alex"), "xelA")
    
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_palindrome_string(self):
        self.assertEqual(reverse_string("savvas"), "savvas")

    if __name__ == '__main__':
        unittest.main()

