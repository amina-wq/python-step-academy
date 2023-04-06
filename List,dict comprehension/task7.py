# Создайте вложенный список размером 3*3 через функцию. 
# И посчитайте сумму элементов главной диагонали. 

import random

def create_random_matrix(size: int) -> list[list[int]]:
    matrix = [[random.randint(1, 10) for j in range(size)] for i in range(size)]
    print("Created matrix: ", matrix)
    return matrix

def create_matrix_from_input(size: int) -> list[list[int]]:
    matrix = [[int(input(f'Enter the matrix[{i+1}][{j+1}] element: ')) for j in range(size)] for i in range(size)]
    print("Created matrix:", matrix)
    return matrix

def sum_main_diagonal(matrix: list[list[int]]) -> int:
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum


if __name__ == '__main__':
    print(sum_main_diagonal(create_random_matrix(3)))
    print(sum_main_diagonal(create_matrix_from_input(3)))
