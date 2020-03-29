class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for row in matrix:
            for i in range(1, len(row)):
                row[i] += row[i-1]
        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] += matrix[i-1][j]
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bigSum = self.matrix[row2][col2]
        if row1 > 0:
            bigSum -= self.matrix[row1-1][col2]
        if col1 > 0:
            bigSum -= self.matrix[row2][col1-1]
        if row1 > 0 and col1 > 0:
            bigSum += self.matrix[row1-1][col1-1]

        return bigSum
