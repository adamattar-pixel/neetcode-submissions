class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        for n in nums[1:]:
            if n > currSum + n:
                currSum = n
            else:
                currSum += n
            maxSum = max(currSum, maxSum)
        return maxSum