class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        merged = ""
        while p1 < len(word1) and p2 < len(word2):
            if p1 <= p2:
                merged += word1[p1]
                p1 += 1
            else:
                merged += word2[p2]
                p2 += 1
        merged += word1[p1:]
        merged += word2[p2:]
        return merged