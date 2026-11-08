class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        currMax = nums[i]
        while i <= j:
            m = (i + j) // 2
            if nums[m] > nums[j]:
                i = m + 1
                currMax = min(currMax, nums[j])
            else:
                j = m - 1
                currMax = min(currMax, nums[m])
        return currMax