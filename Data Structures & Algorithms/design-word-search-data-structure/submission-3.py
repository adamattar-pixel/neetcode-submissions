class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.end_of_word = True


    def search(self, word: str) -> bool:
        if not word: return self.end_of_word
        if word[0] == ".":
            atLeastOne = False
            for child in self.children:
                atLeastOne |= self.children[child].search(word[1:]) 
            return atLeastOne
        if word[0] not in self.children: return False
        return self.children[word[0]].search(word[1:])