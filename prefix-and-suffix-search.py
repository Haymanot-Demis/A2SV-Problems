class TrieNode:
    def __init__(self):
        self.kids = {}
        self.isEOW = False
        self.indx = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()

        for indx, word in enumerate(words):
            for i in range(len(word)):
                self.insert(word[i:] + "}" + word, indx)

        
    def insert(self, word, indx):
        node = self.root

        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode()
            
            node = node.kids[ch]
            node.indx = max(node.indx, indx)

        node.isEOW = True
      
    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            if ch not in node.kids:
                return -1

            node = node.kids[ch]
            
        return node.indx

    def f(self, pref: str, suff: str) -> int:
        indx = self.startsWith(suff + "}" + pref)    

        return indx    


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)