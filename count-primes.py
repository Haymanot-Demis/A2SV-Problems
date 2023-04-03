class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        def isPrime(x):
            if x <= 1:
                return False
            d = 2
            while d <= int(x ** 0.5):
                print("r", x % d)
                if x % d == 0:
                    return False
                d += 1
            return True
        primes = [True] * (n - 1)
        for i in range(1, int(n ** 0.5) + 1):
            if isPrime(i):
                for j in range(i * i, n, i):
                    primes[j - 1] = False
            else:
                primes[i - 1] = False
        return primes.count(True)