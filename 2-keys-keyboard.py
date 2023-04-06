class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        d = n // 2
        while d > 1 and n % d:
            d -= 1
        return n // d + self.minSteps(d)