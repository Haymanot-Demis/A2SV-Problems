class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        p = len(needle) - 1

        hashed = 0
        windw = 0
        for i in range(p + 1):
            hashed += (ord(needle[i]) - 96) * (26 ** (p - i))
            windw += (ord(haystack[i]) - 96) * (26 ** (p - i)) 
        
        if hashed == windw:
            return 0
        
        for j in range(p + 1, len(haystack)):
            windw -= (ord(haystack[j - (p + 1)]) - 96) * (26 ** (p))
            windw *= 26
            windw += (ord(haystack[j]) - 96)

            if hashed == windw:
                return j - p
            
        return -1