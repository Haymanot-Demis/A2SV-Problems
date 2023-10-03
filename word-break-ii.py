class TrieNode:
    def __init__(self):
        self.kids = {}
        self.isEOW = False
        self.word = ""

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word) 

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode()
            
            node = node.kids[ch]

        node.isEOW = True
        node.word = word      

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie(wordDict)
        memo = defaultdict(list)
        validity = defaultdict(bool)
        ans = []

        def dpSearch(indx):
            node = trie.root

            if indx == len(s):
                return True, [[]]

            if indx in memo:
                return validity[indx], memo[indx]
        
            for i in range(indx, len(s)):
                ch = s[i]
                if ch in node.kids:
                    node = node.kids[ch]
                    if node.isEOW:
                        isValid, result = dpSearch(i + 1)
                        validity[indx] |= isValid
                        if isValid:
                            for res in result:
                                memo[indx].append([node.word] + res)
                else:
                    return validity[indx], memo[indx]

            return  validity[indx], memo[indx]

        dpSearch(0)

        for sentence in memo[0]:
            ans.append(" ".join(sentence))
            
        return ans