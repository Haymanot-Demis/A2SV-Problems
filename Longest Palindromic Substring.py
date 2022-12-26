class Solution:
    def longestPalindromicSubstring(self, s:str):
        i = 0 
        length = len(s)
        palindrom = ''
        while i < length:
            char = s[i]
            if char in s[i + 1:]:
                substring = s[i:s[i+1:].index(char)]