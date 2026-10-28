class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWord = {}
        for word in strs:
            if str(sorted(word)) in sortedWord:
                sortedWord[str(sorted(word))].append(word)
            else:
                sortedWord[str(sorted(word))] = [word]
        return list(sortedWord.values())
