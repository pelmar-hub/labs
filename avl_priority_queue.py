class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1  # Обов'язкове поле для AVL-дерева


class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def insert(self, value, priority):
        self.root = self._insert_node(self.root, value, priority)

    def _insert_node(self, root, value, priority):
        if not root:
            return Node(value, priority)

        if priority >= root.priority:
            root.left = self._insert_node(root.left, value, priority)
        else:
            root.right = self._insert_node(root.right, value, priority)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        if balance > 1 and priority >= root.left.priority:
            return self._right_rotate(root)
        
        if balance < -1 and priority < root.right.priority:
            return self._left_rotate(root)
        
        if balance > 1 and priority < root.left.priority:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        if balance < -1 and priority >= root.right.priority:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def peek(self):
        if not self.root:
            raise IndexError("Черга з пріоритетами порожня.")
        
        current = self.root
        while current.left:
            current = current.left
            
        return current.value, current.priority

    def extract_max(self):
        if not self.root:
            raise IndexError("Черга з пріоритетами порожня.")
        
        self.root, max_node = self._delete_leftmost(self.root)
        return max_node.value, max_node.priority

    def _delete_leftmost(self, root):
        if not root:
            return root, None
        if not root.left:
            return root.right, root

        root.left, deleted_node = self._delete_leftmost(root.left)

        if not root:
            return root, deleted_node

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._right_rotate(root), deleted_node
            
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root), deleted_node
            
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._left_rotate(root), deleted_node
            
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root), deleted_node

        return root, deleted_node

if __name__ == "__main__":
    pass
