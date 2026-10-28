class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        seen = set()
        m, n = len(board), len(board[0])

        for i in range(0, m):
            if board[i][0] != "O": continue
            board[i][0] = "-"
            queue.append((i, 0))
            seen.add((i, 0))
        for i in range(0, m):
            if board[i][n - 1] != "O": continue
            board[i][n - 1] = "-"
            queue.append((i, n - 1))
            seen.add((i, n - 1))
        for j in range(1, n - 1):
            if board[0][j] != "O": continue
            board[0][j] = "-"
            queue.append((0, j))
            seen.add((0, j))
        for j in range(1, n - 1):
            if board[m - 1][j] != "O": continue
            board[m - 1][j] = "-"
            queue.append((m - 1, j))
            seen.add((m - 1, j))
        
        
        while queue:
            (i, j) = queue.popleft()
            for (k, l) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if not (0 <= k < m and 0 <= l < n and (k, l) not in seen and board[k][l] == "O"): continue
                board[k][l] = "-"
                queue.append((k, l))
                seen.add((k, l))
        
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == "O": board[i][j] = "X"
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == "-": board[i][j] = "O"

        