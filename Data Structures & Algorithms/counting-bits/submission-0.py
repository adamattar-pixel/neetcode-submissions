class Solution:
    def countBits(self, n: int) -> List[int]:
        toRet = [0]*(n+1)
        for i in range(0, n+1):
            j = i
            while j != 0:
                if j % 2 == 1:
                    toRet[i] += 1
                j = j // 2
            
        return toRet