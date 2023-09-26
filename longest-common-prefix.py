class TrieNode:
    def __init__(self):
        self.kids = [None for _ in range(26)]
        self.isEOW = False
class Trie:

    def __init__(self):
        self.root = TrieNode()    

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            indx = ord(ch) - ord('a')

            if not node.kids[indx]:
                node.kids[indx] = TrieNode()
            
            node = node.kids[indx]

        node.isEOW = True



    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            indx = ord(ch) - ord('a')

            if not node.kids[indx]:
                return False
            
            return node.isEOW
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            indx = ord(ch) - ord('a')

            if not node.kids[indx]:
                return False
            
            return True
        
    def longestCommonPrefix(self):
        node = self.root
        count = 0
        prefix = ""
        while not node.isEOW and node.kids.count(None) == 25:
            for i, ch in enumerate(node.kids):
                if ch:
                    prefix += chr(ord('a') + i)
                    node = ch
                    break
        return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""

        trie = Trie()

        for s in strs:
            trie.insert(s)
        print(trie.root)
        return trie.longestCommonPrefix()