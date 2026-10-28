class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1: return ["()"]
        prev = self.generateParenthesis(n-1)
        toRet = dict()
        for parent in prev:
            for i in range(0, len(parent) + 1):
                t = "(" + parent[0:i] + ")" + parent[i:]
                toRet[t] = t
        return list(toRet.values())