class Solution:
    def myPow(self, x: float, n: int) -> float:
        """"
        recursivelly call the function with exponent less than current exponent by one by multiplying with the number if we have even exponent we can make the number square and make the exponent halfed 
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n  = -n         
        if n % 2 == 0:
            return self.myPow(x*x, n//2)
        return x*self.myPow(x, n - 1)