class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x : len(x))
        long_chain = 1
        memo = [1] * len(words)

        for i in range(len(words)):
            for j in range(i):
                if self.isPredecessor(words[j], words[i]):
                    memo[i] = max(memo[i], memo[j] + 1)
        return max(memo)
                

    def isPredecessor(self, wordA, wordB):
        lB = len(wordB)
        lA = len(wordA)
        
        if lB <= lA or lA <= lB - 2:
            return False

        diff_count = 0
        i = 0
        while i < lB - 1:
            if wordB[i] != wordA[i]:
                if diff_count != 0:
                    return False
                diff_count += 1
                wordB = wordB[:i] + wordB[i+1:]
                continue
            i += 1
        return True