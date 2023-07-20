class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = defaultdict(int)
        def dp(indx1, indx2):
            if indx1 == len(text1) or indx2 == len(text2):
                return 0

            if (indx1, indx2) in memo:
                return memo[(indx1, indx2)]
            
            if text1[indx1] == text2[indx2]:
                memo[(indx1, indx2)] = dp(indx1 + 1, indx2 + 1) + 1
            else:
                memo[(indx1, indx2)] = max(dp(indx1 + 1, indx2), dp(indx1, indx2 + 1))
            return memo[(indx1, indx2)]
        
        return dp(0, 0)