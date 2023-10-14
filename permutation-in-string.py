class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needleHash = Counter(s1)
        windwHash = Counter(s2[:len(s1) - 1])

        for i in range(len(s1) - 1, len(s2)):
            windwHash[s2[i]] += 1

            if needleHash == windwHash:
                return True
            windwHash[s2[i + 1 - len(s1)]] -= 1
            if windwHash[s2[i + 1 - len(s1)]] == 0:
                del windwHash[s2[i + 1 - len(s1)]]
            
        return False