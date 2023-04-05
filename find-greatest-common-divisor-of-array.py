class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def GCD(a, b):
            while a and b:
                if a > b:
                    a = a % b
                else:
                    b = b % a
            return max(a, b) 
        return GCD(min(nums), max(nums))