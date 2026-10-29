class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for i in range(k):
            if i < len(nums):
                heapq.heappush(self.h, nums[i])
        for num in nums[k:]:
            heapq.heappush(self.h, num)
            if len(self.h) > k:
                heapq.heappop(self.h)


    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]