#time 5
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        bit_len = n.bit_length()

        if n.bit_count() == 1: # it must have only one set bit
            print("dsf")
            return bit_len % 2 == 1 # it is power of two of power of two number so the position must be even but since bit starts from zero from right it must be odd to be power of 4
        return False