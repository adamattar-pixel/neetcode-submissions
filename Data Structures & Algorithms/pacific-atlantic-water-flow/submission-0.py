class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        queueAtl = deque()
        seenAtl = set()
        m, n = len(heights), len(heights[0])
        for i in range(m):
            queueAtl.append((i, n - 1))
            seenAtl.add((i, n - 1))
        for j in range(n - 1):
            queueAtl.append((m - 1, j))
            seenAtl.add((m - 1, j))

        while queueAtl:
            (i, j) = queueAtl.popleft()
            for (k, l) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not (0 <= k < m and 0 <= l < n and (k, l) not in seenAtl and heights[k][l] >= heights[i][j]): continue
                seenAtl.add((k, l))
                queueAtl.append((k, l))
        
        queuePac = deque()
        seenPac = set()
        for i in range(m):
            queuePac.append((i, 0))
            seenPac.add((i, 0))
        for j in range(1, n):
            queuePac.append((0, j))
            seenPac.add((0, j))

        while queuePac:
            (i, j) = queuePac.popleft()
            for (k, l) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not (0 <= k < m and 0 <= l < n and (k, l) not in seenPac and heights[k][l] >= heights[i][j]): continue
                seenPac.add((k, l))
                queuePac.append((k, l))
        
        return list(seenPac.intersection(seenAtl))