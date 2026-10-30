class Solution:
    def canJump(self, nums: List[int]) -> bool:
        slow = 0
        fast = 0
        while slow <= fast:
            fast = max(nums[slow] + slow, fast)
            slow += 1
            if fast >= len(nums) - 1: return True
        return False