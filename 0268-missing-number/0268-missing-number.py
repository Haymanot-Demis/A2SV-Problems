from collections import Counter
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashed = Counter(nums)
        for i in range(len(nums) + 1):
            if hashed.get(i, 0) == 0:
                return i       