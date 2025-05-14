import unittest
from my_functions import add, subtract

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 555)
    
    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)
    
    def test_zero(self):
        self.assertEqual(add(0, 7), 7)
    
class TestSubtract(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(subtract(4, 3), 1)
    
    def test_negative(self):
        self.assertEqual(subtract(-4, -3), -1)

    def test_zero(self):
        self.assertEqual(subtract(0,3), -3)

    if __name__== '__main__':
        unittest.main()
    
