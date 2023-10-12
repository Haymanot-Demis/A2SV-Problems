class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        LPS = [0] * len(needle)

        def KMP_LPS():
            j = 0
            i = 1
            while i < len(needle):
                if needle[i] == needle[j]:
                    LPS[i] = j + 1
                    j += 1
                    i += 1
                else:
                    if j == 0:
                        i += 1
                    else:
                        j = LPS[j - 1]
        KMP_LPS()

        j = 0
        i = 0
        l1 = len(haystack)
        l2 = len(needle)
        
        while i < l1 and j < l2:
            if needle[j] != haystack[i]:
                if j > 0:
                    j = LPS[j - 1]
                else:
                    i += 1
            else:
                i += 1
                j += 1
        
        if j == l2:
            return i - l2

        return -1