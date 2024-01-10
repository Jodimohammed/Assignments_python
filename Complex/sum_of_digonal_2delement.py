#python program to sum diagonal elements in a list ..

def sum_diagonal_elements(matrix):
    diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
    return diagonal_sum



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = sum_diagonal_elements(matrix)
print(f"The sum of diagonal elements is: {result}")
