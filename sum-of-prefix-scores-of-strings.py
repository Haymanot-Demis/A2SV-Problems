class TrieNode:
    def __init__(self):
        self.kids = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()    

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode()
            
            node = node.kids[ch]
            node.count += 1

    def Score(self, word: str) -> bool:
        node = self.root
        score = 0

        for ch in word:
            if ch not in node.kids:
                return False
            
            node = node.kids[ch]
            score += node.count
            
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        answer = []
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        for word in words:
            answer.append(trie.Score(word))
        
        return answer