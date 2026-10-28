class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            occurenceList = [0] * 26
            for char in word:
                occurenceList[ord(char) - ord('a')] += 1
            group[tuple(occurenceList)].append(word)
        return list(group.values())