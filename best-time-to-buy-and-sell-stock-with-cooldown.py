class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bottom up
        memo = {}
        for i in range(len(prices)):
            temp_memo = dict(memo)
            temp_memo[(i, 1)] = -prices[i]
            temp_memo[(i, 3)] = 0
            temp_memo[(i, 2)] = 0

            for key, profit in memo.items():
                indx, state = key
                if state == 1:
                    temp_memo[(i, 2)] = max(temp_memo[(i, 2)], profit + prices[i])
                elif state == 3:
                    temp_memo[(i, 1)] = max(temp_memo[(i, 1)], profit - prices[i])
                else:
                    temp_memo[(i, 3)] = max(temp_memo[(i, 3)], profit)
                
            memo = temp_memo
        return max(memo.values())

        # Top down
        # def dp(indx, state):
        #     # state can be sell(1), buy(2) or cooldown(3)
        #     if (indx,state) in memo:
        #         return memo[(indx, state)]
            
        #     if indx >= len(prices):
        #         return 0

        #     profit = 0
        #     if state == 1:    
        #         profit = max(profit, dp(indx + 1, state))
        #         profit = max(profit, dp(indx + 1, 2) - prices[indx])
        #     else:
        #         profit = max(profit, dp(indx + 1, state))
        #         profit = max(profit, dp(indx + 2, 1) + prices[indx])
        #     memo[(indx, state)] = profit

        #     return profit
        # return dp(0, 1)