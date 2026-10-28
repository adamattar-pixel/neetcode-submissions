class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        dist = {}
        maxim = 0
        ones = 0
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1: ones += 1
                if grid[i][j] == 2:
                    dist[(i, j)] = 0
                    queue.append((i, j))
        
        onesReachable = 0

        while queue:
            (i, j) = queue.popleft()
            for (k, l) in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
                if not (0 <= k < len(grid) and 0 <= l < len(grid[0]) and grid[k][l] == 1 and (k, l) not in dist):
                    continue
                onesReachable += 1
                dist[(k, l)] = dist[(i, j)] + 1
                maxim = max(maxim, dist[(k, l)])
                queue.append((k, l))

        return maxim if ones == onesReachable else -1