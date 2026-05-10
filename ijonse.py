import sys
import os

def solve():
    # Перевіряємо, чи є файл взагалі
    if not os.path.exists('ijones.in'):
        print("Помилка: Файл ijones.in не знайдено! Перевір назву.")
        return

    with open('ijones.in', 'r') as f_in:
        data = f_in.read().split()
        if not data: return
        W, H = int(data[0]), int(data[1])
        grid = data[2:]

    print(f"Зчитано поле {W}x{H}. Рахую...")

    dp_prev = [1] * H
    char_sums = {}
    for r in range(H):
        char_sums[grid[r][0]] = char_sums.get(grid[r][0], 0) + 1

    for c in range(1, W):
        dp_curr = [0] * H
        col_updates = {}
        for r in range(H):
            curr_char = grid[r][c]
            ways = char_sums.get(curr_char, 0)
            if curr_char != grid[r][c-1]:
                ways += dp_prev[r]
            dp_curr[r] = ways
            col_updates[curr_char] = col_updates.get(curr_char, 0) + ways
        
        for char, val in col_updates.items():
            char_sums[char] = char_sums.get(char, 0) + val
        dp_prev = dp_curr

    result = dp_prev[0] if H == 1 else dp_prev[0] + dp_prev[H-1]
    
    with open('ijones.out', 'w') as f_out:
        f_out.write(str(result) + '\n')
    
    print(f"Готово! Результат {result} записано в ijones.out")

if __name__ == "__main__":
    solve()