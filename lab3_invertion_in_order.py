import os

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def get_successor(self):
        if self.right is not None:
            curr = self.right
            while curr.left is not None:
                curr = curr.left
            return curr

        curr = self
        parent = self.parent
        while parent is not None and parent.right == curr:
            curr = parent
            parent = parent.parent
        return parent

    @classmethod
    def build_from_inorder(cls, inorder_list, parent=None):
        if not inorder_list:
            return None
        mid_index = len(inorder_list) // 2
        node = cls(inorder_list[mid_index], parent=parent)
        
        node.left = cls.build_from_inorder(inorder_list[:mid_index], parent=node)
        node.right = cls.build_from_inorder(inorder_list[mid_index + 1:], parent=node)
        
        return node

    def print_reverse_inorder(self):
        if self.right is not None:
            self.right.print_reverse_inorder()
            
        print(self.value, end=' ')
        
        if self.left is not None:
            self.left.print_reverse_inorder()

    def find_node(self, target):
        if target == self.value:
            return self
        elif target < self.value and self.left:
            return self.left.find_node(target)
        elif target > self.value and self.right:
            return self.right.find_node(target)
        return None

def process_tree_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().split()
            inorder_data = [int(x) for x in data]
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
        return

    root = BinaryTree.build_from_inorder(inorder_data)

    if root is not None:
        print("Вивід дерева у зворотньому порядку:")
        root.print_reverse_inorder()



if __name__ == "__main__":
    test_filename = "invertion_in_order_tree_data.txt"
    process_tree_file(test_filename)