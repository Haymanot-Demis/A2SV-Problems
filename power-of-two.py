class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        one_bits_count = 0 # counting the number of 1's in the binary representation
        while n:
            one_bits_count += 1
            n = n & (n - 1)
        return True if one_bits_count == 1 else False