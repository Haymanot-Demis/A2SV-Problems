#time 70
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        srcHash = dict(collections.Counter(p))
        windowSize = len(p)
        windowEnd = windowSize - 1
        windowStart = 0
        length = len(s)
        anagram = s[windowStart:windowEnd]
        anagramHash = dict(collections.Counter(anagram))
        indices = []
        while windowEnd < length:
            anagramHash[s[windowEnd]] = anagramHash.get(s[windowEnd],0) + 1
            anagram += s[windowEnd]
            if anagramHash == srcHash:
                indices.append(windowStart)
            anagramHash[s[windowStart]] -= 1
            if anagramHash[s[windowStart]] == 0:
                anagramHash.pop(s[windowStart])
            anagram = anagram[1:]
            windowStart += 1
            windowEnd += 1
            
        return indices