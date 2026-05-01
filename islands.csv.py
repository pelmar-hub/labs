import csv

def solve_mst():
    adj_matrix = []
    try:
        with open('islands.txt', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                adj_matrix.append([float(x) for x in row])
    except FileNotFoundError:
        print("Помилка: Файл islands.csv не знайдено!")
        return

    n = len(adj_matrix)
    if n == 0: return

    selected_node = [False] * n
    selected_node[0] = True
    num_edges = 0
    total_length = 0

    while (num_edges < n - 1):
        minimum = float('inf')
        x = 0
        y = 0
        
        for i in range(n):
            if selected_node[i]:
                for j in range(n):
                    if not selected_node[j] and adj_matrix[i][j] > 0:
                        if minimum > adj_matrix[i][j]:
                            minimum = adj_matrix[i][j]
                            x, y = i, j
        
        if minimum == float('inf'):
            print("Граф не зв'язний! Неможливо з'єднати всі острови.")
            break

        total_length += minimum
        selected_node[y] = True
        num_edges += 1

    print(f"Мінімальна довжина кабелів: {total_length}")

if __name__ == "__main__":
    solve_mst()