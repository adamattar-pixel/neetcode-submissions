class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):

                if grid[i][j] == "1":
                    number += 1
                    grid[i][j] = "0"
                    stack = self.oneNeighbors(i, j, grid)
                    while stack:
                        (k, l) = stack.pop()
                        if grid[k][l] == "0": continue
                        grid[k][l] = "0"
                        stack += self.oneNeighbors(k, l, grid)
        return number
                    

    def oneNeighbors(self, i: int, j: int, grid: List[List[str]]) -> list:
        return [(k, l) 
        for (k, l) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        if 0 <= k and k < len(grid)
        if 0 <= l and l < len(grid[0])
        if grid[k][l] == "1"]