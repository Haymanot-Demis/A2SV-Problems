class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime_factors = set()
        for num in nums:
            d = 2
            while d * d <= num:
                if num % d == 0:
                    prime_factors.add(d)
                    num //=d
                else:
                    d += 1
            if num > 1:
                prime_factors.add(num)
        return len(prime_factors)