class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        length = len(s)
        l = 0
        r = 0
        lis = defaultdict(list)
        curr = 0
        maxim = 0
        while r < length:
            curr += 1
            if lis[s[r]] == True:
                while s[l] != s[r] and l < r:
                    lis[s[l]] = False
                    l += 1
                    curr -=1
                curr -= 1
                l += 1
            else:
                lis[s[r]] = True
            maxim = max(maxim, curr)
            r += 1
        return maxim