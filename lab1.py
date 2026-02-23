import unittest
def rb( matrix):
    result = []
    for m in range(len(matrix)):
            if m % 2 == 0:
                result.extend(matrix[m])
            else:
                result.extend(matrix[m][::-1])
    return result

class TestRbRoutine(unittest.TestCase):
    def test_m5_n5(self):
         matrix = [[(i * 5 + j + 1) for j in range(5)] for i in range(5)]
         result = rb(matrix)
         self.assertEqual(len(result), 25)
         self.assertEqual(result[0], 1)
         self.assertEqual(result[5], 10)
         self.assertEqual(result[24], 25)     
    def test_m2_n4(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
        expected = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(rb(matrix), expected)  
    def test_m6_n1(self):
        matrix = [[1], [2], [3], [4], [5], [6]]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(rb(matrix), expected)         
if __name__ == '__main__':   unittest.main()
