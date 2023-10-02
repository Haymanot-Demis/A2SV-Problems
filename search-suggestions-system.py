class TrieNode:
    def __init__(self):
        self.kids = {}
        self.indices = []

class Trie:
    def __init__(self):
        self.root = TrieNode()    

    def insert(self, word, indx) -> None:
        node = self.root

        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode()
            
            node = node.kids[ch]
            if len(node.indices) < 3:
                node.indices.append(indx)
    def prefixSearch(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.kids:
                return []
            node = node.kids[ch]
            
        return node.indices

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()
        for indx, prod in enumerate(products):
            trie.insert(prod, indx)
        
        suggestion = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            res = trie.prefixSearch(prefix)
            w = []
            for indx in res:
                w.append(products[indx])
                
            suggestion.append(w)
        
        return suggestion