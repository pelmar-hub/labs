import os
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, val):
        if val < self.value:
            if self.left is None:
                self.left = BinaryTree(val, parent=self)
            else:
                self.left.insert(val)
        elif val > self.value:
            if self.right is None:
                self.right = BinaryTree(val, parent=self)
            else:
                self.right.insert(val)

    @classmethod
    def build_from_list(cls, data_list):
        if not data_list:
            return None
            
        root = cls(data_list[0])
        for value in data_list[1:]:
            root.insert(value)
            
        return root

def draw_tree_in_console(root_node):
    def _display_aux(node):
        if getattr(node, 'right', None) is None and getattr(node, 'left', None) is None:
            line = '%s' % node.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if getattr(node, 'right', None) is None:
            lines, n, p, x = _display_aux(node.left)
            s = '%s' % node.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if getattr(node, 'left', None) is None:
            lines, n, p, x = _display_aux(node.right)
            s = '%s' % node.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = _display_aux(node.left)
        right, m, q, y = _display_aux(node.right)
        s = '%s' % node.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    if not root_node:
        return
        
    lines, *_ = _display_aux(root_node)
    for line in lines:
        print(line)

def main():
    filename = "invertion_in_order_tree_data.txt"
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read().split()
            original_list = [int(x) for x in data]
        reversed_list = original_list[::-1]
        
        print("Вивід списку у зворотньому порядку:")
        for num in reversed_list:
            print(num, end=" ")
        print("\n")
        
        root = BinaryTree.build_from_list(reversed_list)
        
        if root:
            print("Графічне відображення дерева:")
            draw_tree_in_console(root)
            print()
            
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено!")
    except ValueError:
        print("Помилка: У файлі мають бути лише числа.")

if __name__ == "__main__":
    main()
