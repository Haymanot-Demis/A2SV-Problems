class TrieNode:
    def __init__(self):
        self.kids = {}
        self.isEOW = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.root.isEOW = True

    def insert(self, word) -> None:
        node = self.root

        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode()
            
            node = node.kids[ch] 
        
        node.isEOW = True

    def longestWord(self, prev="", node=None):
        if not node:
            return self.longestWord("", self.root)

        words = []

        if not len(node.kids):
            words.append(prev)

        for ch, kid in node.kids.items():
            if kid.isEOW:
                words.extend(self.longestWord(prev + ch, kid))
            else:
                words.append(prev)
        
        return words


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        answers = trie.longestWord()

        if not answers:
            return ""

        answers.sort(reverse=True)
        ans = answers[0]

        for word in answers:
            if len(word) >= len(ans):
                ans = word        
        
        return ans