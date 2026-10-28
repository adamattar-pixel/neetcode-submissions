class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict()
        for word in strs:
            occurenceList = [0] * 26
            for char in word:
                occurenceList[ord(char) - ord('a')] += 1
            if tuple(occurenceList) in group:
                group[tuple(occurenceList)].append(word)
            else:
                group[tuple(occurenceList)] = [word]
        return list(group.values())