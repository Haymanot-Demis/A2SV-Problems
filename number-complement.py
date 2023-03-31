class Solution:
    def findComplement(self, num: int) -> int:
        complement = 0
        i = 0
        while num != 0:
            if not (num & 1):
                complement += 2 ** i
            i += 1
            num >>= 1
        return complement