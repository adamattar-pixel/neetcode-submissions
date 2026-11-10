class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newNums = sorted(nums)
        seen = defaultdict(list)
        currMax = 0
        for n in newNums:
            if n - 1 not in seen:
                seen[n] = 1
                currMax = max(currMax, 1)
            elif n not in seen:
                seen[n] = seen[n - 1] + 1
                currMax = max(currMax, seen[n])
            else:
                seen[n] = max(seen[n], seen[n - 1] + 1)
                currMax = max(currMax, seen[n])
        return currMax