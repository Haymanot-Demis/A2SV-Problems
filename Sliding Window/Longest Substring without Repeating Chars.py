#time = 30
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = 0
        windowEnd = 0
        longestSize = 0
        longestSubstring = ''
        length = len(s)
        while windowEnd < length:
            if s[windowEnd] in s[windowStart:windowEnd]:
                if windowEnd - windowStart > longestSize:
                    longestSize = windowEnd - windowStart
                    longestSubstring = s[windowStart:windowEnd]
                print(s[windowStart:windowEnd], s[windowEnd])
                windowStart += s[windowStart:windowEnd].index(s[windowEnd]) + 1
                print(windowStart)
            elif windowEnd + 1 == length:
                windowEnd += 1
                if windowEnd - windowStart > longestSize:
                    longestSize = windowEnd - windowStart
                    longestSubstring = s[windowStart:windowEnd]
                    windowStart = windowEnd
            windowEnd += 1

        return longestSize