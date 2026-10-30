class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = [newInterval]
        for i, interval in enumerate(intervals):
            top = stack.pop()
            if interval[1] < top[0]:
                stack.append(interval)
                stack.append(top)
            elif interval[0] > top[1]:
                stack = stack + [top, interval] + intervals[i + 1:]
                break
            else:
                stack.append([min(interval[0], top[0]), max(interval[1], top[1])])
        return stack
