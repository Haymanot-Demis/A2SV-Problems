class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:0, 1:1, 2:2, 3:3}
        if n <= 3:
            return n
            
        for i in range(4, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n]