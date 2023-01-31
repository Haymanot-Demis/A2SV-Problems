class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        p1 = 0
        p2 = 0
        merge = ""
        while p1 < l1 and p2 < l2:
            if word1[p1:] > word2[p2:]:
                merge += word1[p1]
                p1 += 1
            else:
                merge += word2[p2]
                p2 += 1
        merge += word1[p1:]
        merge += word2[p2:]
        
        return merge


        