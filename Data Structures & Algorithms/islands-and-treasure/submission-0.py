class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        seen = set()
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    seen.add((i, j))
        while queue:
            (i, j) = queue.pop(0)
            for (k, l) in [(i + 1, j), (i - 1, j), (i, j + 1),(i, j - 1)]:
                if not (0 <= k < len(grid) and 0 <= l < len(grid[0]) and grid[k][l] != -1 and (k, l) not in seen): continue
                queue.append((k, l))
                seen.add((k, l))
                grid[k][l] = grid[i][j] + 1
        