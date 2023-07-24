class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(indx, state):
            # state can be sell(1), buy(2) or cooldown(3)
            if (indx,state) in memo:
                return memo[(indx, state)]
            
            if indx >= len(prices):
                return 0

            profit = 0
            if state == 1:    
                profit = max(profit, dp(indx + 1, state))
                profit = max(profit, dp(indx + 1, 2) - prices[indx])
            else:
                profit = max(profit, dp(indx + 1, state))
                profit = max(profit, dp(indx + 2, 1) + prices[indx])
            memo[(indx, state)] = profit

            return profit
        return dp(0, 1)