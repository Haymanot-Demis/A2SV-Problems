class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_day = [prices[-1]] * len(prices)
        
        for i in range(len(prices) - 2, -1, -1):
            max_profit_day[i] = max(max_profit_day[i + 1], prices[i])

        max_profit = 0

        for i in range(len(prices)):
            max_profit = max(max_profit, max_profit_day[i] - prices[i])
        
        return max_profit