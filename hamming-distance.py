class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0
        while x or y:
            if x & 1 != y & 1:
                hamming_distance += 1
            x >>= 1
            y >>= 1
        return hamming_distance