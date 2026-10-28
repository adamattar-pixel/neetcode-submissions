class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    currArea = 1
                    stack = self.neighbors(i, j, grid)
                    while stack:
                        (k, l) = stack.pop()
                        currArea += 1
                        grid[k][l] = 0
                        stack |= self.neighbors(k, l, grid)
                        
                    maxArea = max(maxArea, currArea)
        return maxArea

        
    def neighbors(self, i: int, j: int, grid: List[List[int]]) -> list:
        return set([(k, l) 
        for (k, l) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        if 0 <= k < len(grid) and 0 <= l < len(grid[0])
        if grid[k][l] == 1])