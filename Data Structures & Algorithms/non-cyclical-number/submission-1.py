class Solution:
    def isHappy(self, n: int) -> bool:
        v = self.aux(n)
        m = set()
        while v != 1:
            m.add(v)
            n = v
            v = self.aux(v)
            if v in m: return False
        if v == 1: return True
        return False
        
    def aux(self, n: int) -> int:
        i = 0
        while n != 0:
            i += (n % 10)**2
            n = n // 10
        return i