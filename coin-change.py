class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        result = self.backtrack(coins, amount, memo)
        if result == inf:
            return -1
        return result
    def backtrack(self,coins, amount, memo):
        if amount in memo:
            return memo[amount]

        if amount == 0:
            return 0
        
        if amount < 0:
            return inf

        count = inf        
        for i in range(len(coins)):
            res = self.backtrack(coins, amount - coins[i], memo)
            count = min(count, res + 1)

        memo[amount] = count
        return count