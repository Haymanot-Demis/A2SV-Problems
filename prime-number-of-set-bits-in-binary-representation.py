class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        answer = 0
        for num in range(left, right + 1):
            count_set_bits = 0 
            while num:
                count_set_bits += 1
                num = num & (num - 1)
            if count_set_bits > 1 and isPrime(count_set_bits):
                answer += 1
        return answer