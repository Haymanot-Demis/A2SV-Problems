class Solution:
    def longestPrefix(self, s: str) -> str:
        LPS = [0] * len(s)

        i = 1
        prevLPS = 0

        while i < len(s):
            if s[i] == s[prevLPS]:
                LPS[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            else:
                if prevLPS == 0:
                    i += 1
                else:
                    prevLPS = LPS[prevLPS - 1]
        
        return s[:LPS[-1]]