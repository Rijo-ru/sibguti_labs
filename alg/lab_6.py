def find_max_element(matrix):
    max_val = matrix[0][0]
    max_row, max_col = 0, 0
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_row, max_col = i, j
                
    return max_row, max_col

def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def swap_columns(matrix, col1, col2):
    for i in range(len(matrix)):
        matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

def move_max_to_a00(matrix):
    max_row, max_col = find_max_element(matrix)
    
    swap_rows(matrix, 0, max_row)
    swap_columns(matrix, 0, max_col)

# Пример использования
A = [
    [3, 5, 7],
    [2, 8, 4],
    [1, 9, 6]
]

print("Исходная матрица:")
for row in A:
    print(row)

move_max_to_a00(A)

print("\nМатрица после перемещения максимального элемента:")
for row in A:
    print(row)
