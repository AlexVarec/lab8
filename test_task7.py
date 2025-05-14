import unittest
from my_functions import sort_numbers

class TestSortNumbers(unittest.TestCase):
    def test_already_sorted(self):
        self.assertEqual(sort_numbers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(sort_numbers([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_with_duplicates(self):
        self.assertEqual(sort_numbers([3, 1, 2, 4, 2]), [1, 2, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(sort_numbers([]), [])

if __name__ == '__main__':
    unittest.main()