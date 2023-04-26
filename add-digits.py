class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num_str = str(num)
            num = 0
            for digit in num_str:
                num += int(digit)
        return num