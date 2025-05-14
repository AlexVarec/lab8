import unittest
from my_functions import find_max

class TestFindMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(find_max([-1, -2, -3, -4, -5]), -1)

    def test_single_element(self):
        self.assertEqual(find_max([22]), 22)

    def test_sorted_list(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)

    def test_reverse_sorted_list(self):
        self.assertEqual(find_max([5, 4, 3, 2, 1]), 5)
        

if __name__ == '__main__':
    unittest.main()