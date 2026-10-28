class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for k in range(0, 3):
            for l in range(0, 3):
                s1 = list()
                for i in range(0, 3):
                    for j in range(0, 3):
                        if board[i + 3*k][j + 3*l] in s1: return False
                        if board[i + 3*k][j + 3*l] != ".":
                            s1 += (board[i+3*k][j+3*l])
        
        for i in range(0, 9):
            s2 = list()
            for j in range(0, 9):
                if board[i][j] in s2: return False
                if board[i][j] != ".":
                    s2 += (board[i][j])

        for i in range(0, 9):
            s3 = list()
            for j in range(0, 9):
                if board[j][i] in s3: return False
                if board[j][i] != ".":
                    s3 += (board[j][i])
        
        return True