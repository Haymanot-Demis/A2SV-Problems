class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.dfs(prices, fee, 0, False, {})    
    def dfs(self, prices, fee, indx, flag, memo):
        if indx >= len(prices):
            return 0

        if (indx, flag) not in memo:
            if flag:
                sell = self.dfs(prices, fee, indx + 1, False, memo) +prices[indx] - fee
                not_sell = self.dfs(prices, fee, indx + 1, True, memo)

                memo[(indx, flag)] = max(sell, not_sell)
            else:
                buy = self.dfs(prices, fee, indx + 1, True, memo)-prices[indx]
                not_buy = self.dfs(prices, fee, indx + 1, False, memo)
                memo[(indx, flag)] = max(buy, not_buy)
        return memo[(indx, flag)]