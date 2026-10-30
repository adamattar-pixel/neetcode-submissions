class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = [-s for s in stones]
        heapq.heapify(l)
        while len(l) > 1:
            x = heapq.heappop(l)
            y = heapq.heappop(l)
            if x == y: continue
            heapq.heappush(l, -abs(y-x))
        if not l: return 0
        return -l[0]