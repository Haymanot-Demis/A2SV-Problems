class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = 0
        windowEnd = 0
        longestSize = 0
        longestSubstring = ''
        length = len(s)
        while windowEnd < length:
            if s[windowEnd] in s[windowStart:windowEnd]:
                longestSize = max(windowEnd - windowStart, longestSize)
                # if longestSize < windowEnd - windowStart => longestSubstring = s[windowStart:windowEnd]
                windowStart += s[windowStart:windowEnd].index(s[windowEnd]) + 1
            elif windowEnd + 1 == length:
                windowEnd += 1
                longestSize = max(windowEnd - windowStart, longestSize)
                # longestSubstring = s[windowStart:windowEnd]
                windowStart = windowEnd
            windowEnd += 1

        return longestSize