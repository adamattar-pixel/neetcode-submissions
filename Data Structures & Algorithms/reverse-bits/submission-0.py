class Solution:
    def reverseBits(self, n: int) -> int:
        i = 31
        toRet = 0
        while i >= 0:
            toRet += ((n >> (31- i)) & 1) << i
            i -= 1
        return toRet