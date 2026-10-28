class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        toRet = []
        for i in range(0, 2**len(nums)):
            toAdd = []
            j = i
            for k in range(0, 32):
                if j % 2:
                    toAdd.append(nums[k])
                j = j // 2
            toRet.append(toAdd)
        return toRet