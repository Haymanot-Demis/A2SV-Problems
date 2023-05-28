class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0] * max(n + 1, 3)
        memo[0], memo[1], memo[2] = 0, 1, 1
        def trib(n):
            if n <= 2:
                return memo[n]
            if memo[n] != 0:
                return memo[n]
            memo[n] = trib(n - 1) +  trib(n - 2) + trib(n - 3)
            return memo[n]
        return trib(n)