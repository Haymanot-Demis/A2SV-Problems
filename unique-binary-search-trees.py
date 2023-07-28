class Solution:
    def numTrees(self, n: int) -> int:
        memo = defaultdict(int, {0:1, 1:1, 2:2})
        def dp(n):
            if n in memo:
                return memo[n]
            for i in range(n):
                memo[n] += dp(i) * dp(n - 1 - i)

            return memo[n]
        return dp(n)