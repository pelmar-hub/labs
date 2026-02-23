from lab1 import rb
import unittest

def time_rb(matrix):
    rows = len(matrix)
    if rows == 0:
        return 0
    TIME_PER_ROW = 10
    TIME_PER_TURN = 15
    WORK_INTERVAL = 50
    REST_DURATION = 10
    processing_time = rows * TIME_PER_ROW
    turns_count = max(0, rows - 1)
    turning_time = turns_count * TIME_PER_TURN
    total_active_time = processing_time + turning_time

    if total_active_time > 0:
        number_results = (total_active_time - 1) // WORK_INTERVAL
    else:
        number_results = 0 
    return total_active_time + (number_results * REST_DURATION)     
if __name__ == '__main__':    
    unittest.main(exit=False)
matrix_2x4 = [[1, 2, 3, 4], [5, 6, 7, 8]]
path_2x4 = rb(matrix_2x4)
time_2x4 = time_rb(matrix_2x4)
print("\nМатриця 2x4:")
print(f"Шлях: {path_2x4}")
print(f"Час: {time_2x4} хв")

matrix_6x1 = [[1], [2], [3], [4], [5], [6]]
    
path_6x1 = rb(matrix_6x1)
time_6x1 = time_rb(matrix_6x1)
    
print("\nМатриця 6x1:")
print(f"Шлях: {path_6x1}")
print(f"Час: {time_6x1} хв")        
