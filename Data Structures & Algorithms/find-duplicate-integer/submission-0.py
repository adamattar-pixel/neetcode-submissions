class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = dict()
        for n in nums:
            if n in l: return n
            l[n] = True
        