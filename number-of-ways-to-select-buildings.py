class Solution:
    def numberOfWays(self, s: str) -> int:
        total_zeroes = s.count('0')
        total_ones = s.count('1')

        zeroes_prefix = 0
        ones_prefix = 0

        answer = 0

        for i in range(len(s)):
            if s[i] == '0':
                answer += (total_ones - ones_prefix) * (ones_prefix)
                zeroes_prefix += 1
            else:
                answer += (total_zeroes - zeroes_prefix) * (zeroes_prefix)
                ones_prefix += 1
                
        return answer