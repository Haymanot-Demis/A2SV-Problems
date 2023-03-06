class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        srcHash = dict(collections.Counter(s1))
        windowSize = len(s1)
        windowEnd = windowSize - 1
        windowStart = 0
        length = len(s2)
        permutation = s2[windowStart:windowEnd]
        permutationHash = dict(collections.Counter(permutation))
        while windowEnd < length:
            permutationHash[s2[windowEnd]] = permutationHash.get(s2[windowEnd],0) + 1
            if permutationHash == srcHash:
               return True
            permutationHash[s2[windowStart]] -= 1
            if permutationHash[s2[windowStart]] == 0:
                permutationHash.pop(s2[windowStart])
            windowStart += 1
            windowEnd += 1
        return False