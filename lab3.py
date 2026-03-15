class BinaryTree:
   def __init__(self, value, left=None, right=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
   if node.right is not None:
     curr = node.right
     while curr.left is not None:
       curr = curr.left
     return curr
   curr = node 
   parent = node.parent
   while parent is not None and parent.right == curr:
     curr = parent
     parent = parent.parent
   return parent    
