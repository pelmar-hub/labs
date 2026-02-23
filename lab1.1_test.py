import unittest
from lab1_1 import time_rb

class TestTimeRb(unittest.TestCase):
    def test_normal_case(self):
        test_matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ] 
        result = time_rb(test_matrix)  
        self.assertEqual(result, 70)  

    def test_edge_case(self):
        pass
if __name__ == '__main__':
    unittest.main()