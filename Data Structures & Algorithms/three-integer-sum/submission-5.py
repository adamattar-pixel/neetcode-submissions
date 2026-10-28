class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i, j, k = 0, 0, 0
        toRet = defaultdict(int)
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while k > j:
                target = nums[i] + nums[j] + nums[k]
                if target == 0:
                    toRet[tuple((nums[i], nums[j], nums[k]))] = [nums[i], nums[j], nums[k]]
                    j += 1
                    k -= 1
                elif target < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        return list(toRet.values())

