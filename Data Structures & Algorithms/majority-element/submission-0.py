class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxim = -1
        toRet = -1
        for i in c:
            if c[i] > maxim:
                maxim = c[i]
                toRet = i
        return toRet