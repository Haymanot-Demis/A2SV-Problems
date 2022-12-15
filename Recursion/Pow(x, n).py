class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        return x*self.myPow(x, n - 1)
