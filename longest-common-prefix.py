class TrieNode:
    def __init__(self):
        self.kids = defaultdict(TrieNode)
        self.isEOW = False
class Trie:

    def __init__(self):
        self.root = TrieNode()    

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode()
            
            node = node.kids[ch]

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
        prefix = ""
        while not node.isEOW and len(node.kids) == 1:
            for ch, kids in node.kids.items():
                prefix += ch
                node = kids
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