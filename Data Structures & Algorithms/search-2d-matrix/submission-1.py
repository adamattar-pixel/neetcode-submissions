class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j, m = 0, len(matrix) - 1, -1

        while i <= j:
            m = (i + j) // 2
            if matrix[m][0] < target:
                i = m + 1
            elif matrix[m][0] > target:
                j = m - 1
            else:
                return True
        
        n = j
        i = 0
        j = len(matrix[0]) - 1
        
        while i <= j:
            m = (i + j) // 2
            if matrix[n][m] < target:
                i = m + 1
            elif matrix[n][m] > target:
                j = m - 1
            else:
                return True
        return False