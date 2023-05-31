class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        fibonacci = [0]*(n + 1)
        fibonacci[0], fibonacci[1] = 0, 1

        for state in range(2, n + 1):
            fibonacci[state] = fibonacci[state - 1] + fibonacci[state - 2]  

        return fibonacci[n]