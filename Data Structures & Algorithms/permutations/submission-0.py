class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        subProblem = self.permute(nums[1:])
        toRet = []

        for s in subProblem:
            for i in range(len(s) + 1):
                toRet.append(s[:i] + [nums[0]] + s[i:])
        
        return toRet