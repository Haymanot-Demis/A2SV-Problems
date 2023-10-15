class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def binaryExponentiation(base, exponent):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                half_res = binaryExponentiation(base, exponent // 2)
                return half_res * half_res
            return base * binaryExponentiation(base, exponent - 1)
        
        Pow = 1
        
        currHash = ord(s[0]) - 96
        for i in range(1, k):
            Pow *= power
            val = ord(s[i]) - 96
            currHash += val * Pow
        
        for i in range(k, len(s)):
            if currHash % modulo == hashValue:
                return s[i - k:i]

            prevval = (ord(s[i - k]) - 96)
            currHash = currHash - prevval
            currHash //= power
            currHash += (ord(s[i]) - 96) * Pow
            
        return s[-k:]