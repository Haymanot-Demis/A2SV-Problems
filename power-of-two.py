class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        in the bit concept a power of two is a number with only single 1 bit in its binary representation
        """
        return (n and not(n & (n - 1))) # the and operator is to make sure that the number is not 0