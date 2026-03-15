import unittest
from lab3 import BinaryTree, find_successor
class TestFindSuccessor(unittest.TestCase):
    def test_find_successor(self):
        root = BinaryTree(10)
        root.left =  BinaryTree(5, parent=root)
        root.right = BinaryTree(15, parent=root)
        node3 = BinaryTree(3, parent=root.left)
        node7 = BinaryTree(7, parent=root.left)
        root.left.left = node3
        root.left.right = node7
        node20 = BinaryTree(20, parent=root.right)
        root.right.right = node20


        self.assertEqual(find_successor(root, node3).value, 5)  
        self.assertEqual(find_successor(root, node7).value, 10) 
        self.assertEqual(find_successor(root, root).value, 15)  
        self.assertIsNone(find_successor(root, node20))          
if __name__ == '__main__':
    unittest.main()
print(BinaryTree(10))    