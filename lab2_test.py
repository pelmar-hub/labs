import unittest
from lab2 import has_length
class TestHasLengthRoutine(unittest.TestCase):
    def test (self):
        self.assertTrue(has_length([1, 9, 45 ], 55))
    def test2 (self):
        self.assertTrue(has_length([1, 5, 4, 3, 6], 10))
    def test3 (self):
        self.assertTrue(has_length([1, 2, 4, 3, 6], 9))
    def test4 (self):
        self.assertTrue(has_length([1, 1, 1, 1, 1], 3))        
if __name__ == '__main__':    unittest.main()


