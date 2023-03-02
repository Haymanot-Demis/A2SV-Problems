class StockSpanner:

    def __init__(self):
        self.stock_of_price = []                
    def next(self, price: int) -> int:
        if not self.stock_of_price:
            self.stock_of_price.append((price, 1))
            return 1

        count = 1        
        while self.stock_of_price and self.stock_of_price[-1][0] <= price:
            count += self.stock_of_price.pop()[1]
        self.stock_of_price.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)