class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        curr = 0
        i, j = 0, len(heights) - 1

        while j > i:
            curr = (j - i) * min(heights[i], heights[j])
            maximum = max(maximum, curr)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return maximum