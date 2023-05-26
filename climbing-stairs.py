class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:0, 1:1, 2:2, 3:3}
        if n <= 3:
            return n
        return self.help(n, memo)
        
    def help(self, n: int, memo) -> int:
        if n <= 1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = self.help(n - 1, memo) + self.help(n - 2, memo)
        return memo[n]