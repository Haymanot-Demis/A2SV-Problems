class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        fib1, fib2 = 0, 1

        for state in range(2, n + 1):
            fib2 = fib1 + fib2
            fib1 = fib2 - fib1

        return fib2