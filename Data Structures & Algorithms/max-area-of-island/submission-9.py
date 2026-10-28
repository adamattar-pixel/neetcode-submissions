class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    stack = [(i, j)]
                    currArea = 0

                    while stack:
                        k, l = stack.pop()
                        currArea += 1

                        if k > 0 and grid[k - 1][l] == 1:
                            grid[k - 1][l] = 0
                            stack.append((k - 1, l))

                        if k + 1 < m and grid[k + 1][l] == 1:
                            grid[k + 1][l] = 0
                            stack.append((k + 1, l))

                        if l > 0 and grid[k][l - 1] == 1:
                            grid[k][l - 1] = 0
                            stack.append((k, l - 1))

                        if l + 1 < n and grid[k][l + 1] == 1:
                            grid[k][l + 1] = 0
                            stack.append((k, l + 1))

                    maxArea = max(maxArea, currArea)

        return maxArea