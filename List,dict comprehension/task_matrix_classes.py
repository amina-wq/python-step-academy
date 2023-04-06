# Создайте вложенный список размером 3*3 через функцию. 
# И посчитайте сумму элементов главной диагонали. 
import random


class Matrix:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.matrix = [[random.randint(0, 9) for _ in range(self.col)] for _ in range(self.row)]

    def __str__(self):
        result = 'Matrix:\n'
        for row in self.matrix:
            for value in row:
                result += str(value) + '\t'
            result += '\n'
        return result 


class SquareMatrix(Matrix):
    def __init__(self, dimension: int) -> None:
        super().__init__(dimension, dimension)

    def trace(self) -> int:
        sum = 0
        for i in range(self.row):
            sum += self.matrix[i][i]
        return sum


if __name__ == "__main__":
    m = SquareMatrix(3)
    print(m)
    print(m.trace())
