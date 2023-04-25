class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32
        for num in nums:
            i = 0
            num = abs(num)
            while num:
                bits[i] += 1 & num
                num >>= 1
                i += 1
        number = 0
        for i in range(len(bits)):
            if bits[i] % 3:
                number += (2 ** i)
        if nums.count(number) == 1:
            return number
        return -number