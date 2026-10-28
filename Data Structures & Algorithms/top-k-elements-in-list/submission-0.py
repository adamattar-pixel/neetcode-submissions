class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        n = len(nums)
        B = [[] for x in range(n + 1)]
        for x in c: 
            B[c[x]].append(x)
        result = [x for b in B[::-1] for x in b]
        return result[:k]
        