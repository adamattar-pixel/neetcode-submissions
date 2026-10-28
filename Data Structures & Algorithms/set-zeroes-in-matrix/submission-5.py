class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = 0
        col = 0

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    row |= (1 << i)
                    col |= (1 << j)

        for i in range(0, len(matrix)):
            if row & (1 << i):
                for j in range(0, len(matrix[0])):
                    matrix[i][j] = 0

        for j in range(0, len(matrix[0])):
            if col & (1 << j):
                for i in range(0, len(matrix)):
                    matrix[i][j] = 0

        return None