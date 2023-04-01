class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = ~(n & 1)
        while n != 0:
            if not (n & 1 ^ prev_bit):
                return False
            prev_bit = n & 1
            n >>= 1
        return True