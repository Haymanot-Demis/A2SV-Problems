class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        complement = 0
        i = 0
        while n != 0:
            if not (n & 1):
                complement += 2 ** i
            i += 1
            n >>= 1
        return complement