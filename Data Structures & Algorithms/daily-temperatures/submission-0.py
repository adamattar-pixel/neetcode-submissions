class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        toRet = [0] * len(temperatures)
        stack = list()
        for i, temp in enumerate(temperatures):
            while stack:
                top = stack.pop()
                if top[1] < temp:
                    toRet[top[0]] = i - top[0]
                else:
                    stack.append(top)
                    break
            stack.append([i, temp])
        return toRet
