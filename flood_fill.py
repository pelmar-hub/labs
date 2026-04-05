import ast
from collections import deque
class FloodFiller:
    def __init__(self, input_file = 'input.txt', output_file = 'output.txt'):
        self.input_file = input_file
        self.output_file = output_file
        self.matrix = []
        self.width = 0
        self.height = 0
        self.start_r = 0    
        self.start_c = 0
        self.new_color = ""
    def read_file(self):
        with open(self.input_file, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            self.height, self.width = map(int, lines[0].split(','))
            self.start_r, self.start_c = map(int, lines[1].split(','))
            self.new_color = lines[2].replace('"', '').replace("'", "").replace('‘', '').replace('’', '')  

            for line in lines[3:]:
                if line.endswith(','):
                    line = line[:-1]
                line = line.replace('‘', '').replace('’', '')
                self.matrix.append(ast.literal_eval(line))
    def fill(self):
        target_color = self.matrix[self.start_r][self.start_c]
        if target_color == self.new_color:
            return
        queue = deque([(self.start_r, self.start_c)])
        self.matrix[self.start_r][self.start_c] = self.new_color
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.height and 0 <= nc < self.width and self.matrix[nr][nc] == target_color:
                    self.matrix[nr][nc] = self.new_color
                    queue.append((nr, nc))
    def write_output(self):
        with open(self.output_file, 'w', encoding='utf-8') as f:
            for row in self.matrix:
                row_str = "[" + ", ".join(f"'{color}'" for color in row) + "]"
                f.write(row_str + "\n")                            
if __name__ == "__main__":
    try:
        flood_fill = FloodFiller()
        flood_fill.read_file()
        flood_fill.fill()
        flood_fill.write_output()
        print("Все готово! Результат записан в output.txt")
    except Exception as e:
        print(f"Сталася помилка: {e}")