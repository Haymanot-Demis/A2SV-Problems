class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left == right:
            return [-1, -1]
        sieve = [False, False]
        for i in range(2, right + 1):
            if i % 2 == 0 and i != 2:
                sieve.append(False)
            else:
                sieve.append(True)
        # build the sieve of primes
        for i in range(3, int(right ** 0.5) + 1, 2):
            if sieve[i]:
                for j in range(i ** 2, right + 1, i):
                    sieve[j] = False

        prev_prime = -1
        diff = float("inf")
        num1, num2 = -1, -1
        for i in range(left, right + 1):
            if sieve[i] and prev_prime != -1:
                if i - prev_prime < diff:
                    num1, num2 = prev_prime, i
                    diff = num2 - num1
                prev_prime = i
            elif sieve[i]:
                prev_prime = i
            
        return [num1, num2]