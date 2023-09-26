class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        using the LCS concept, the logest palindromic subsequence is the LCS of s and the reverse of s 
        """ 
        return self.LCS(s, s[::-1])

    def LCS(self, text1, text2):
        """
        LCS with bottom approach is based on the concept of LCS (i, j) is
        1. if text1[i] == text2[j], then we need the LCS of (i - 1, j - 1) and add one
        2. else, LCS of (i, j) will be the maximum of LCS of (i - 1, j) and (i, j - 1)
        """
        memo = defaultdict(int)

        for i in range(len(text1)):       
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    memo[(i, j)] = memo[(i - 1, j - 1)] + 1
                else:
                    memo[(i, j)] = max(memo[(i - 1, j)], memo[(i, j - 1)])
                
        return memo[(len(text1) - 1, len(text2) - 1)]