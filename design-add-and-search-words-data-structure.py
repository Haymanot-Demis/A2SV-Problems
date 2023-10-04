class TrieNode:
    def __init__(self):
        self.kids = {}
        self.isEnd = False
        

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for ch in word:
            if ch not in cur.kids:
                cur.kids[ch] = TrieNode()
                
            cur = cur.kids[ch]
            
        cur.isEnd = True
        
    def dfs(self, indx, cur, word, n):
        if indx < n:
            if word[indx] in cur.kids:
                res = self.dfs(indx + 1, cur.kids[word[indx]], word, n)
                return res
            
            elif word[indx] != ".":
                return False
            else:

                for child in cur.kids:
                    if self.dfs(indx + 1, cur.kids[child], word, n):
                        return True
                
                return False
            
        return cur.isEnd
        
    def search(self, word: str) -> bool:
        cur = self.root
        n = len(word)
        return self.dfs(0, cur, word, n)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)