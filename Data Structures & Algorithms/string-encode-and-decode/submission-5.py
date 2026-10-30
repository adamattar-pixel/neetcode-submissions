class Solution:

    def encode(self, strs: List[str]) -> str:
        toRet = ""
        for s in strs:
            lenToAdd = "00" + str(len(s))
            toRet += lenToAdd[-3:] + s
        return toRet

    def decode(self, s: str) -> List[str]:
        toRet = []
        while s:
            num = int(s[0:3])
            toAdd = s[3:num+3]
            toRet.append(toAdd)
            s = s[num+3:]
        return toRet