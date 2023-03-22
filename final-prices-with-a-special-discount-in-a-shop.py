class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        length = len(prices)
        discount = [0] * length
        stack = []
        
        for i in range(length):
            while stack and prices[i] <= prices[stack[-1]]:
                discount[stack.pop()] = prices[i]
            stack.append(i)
        
        for i in range(length):
            prices[i] -= discount[i]
        return prices