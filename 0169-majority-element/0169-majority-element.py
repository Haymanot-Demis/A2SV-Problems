from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        nums = Counter(nums)
        for num, freq in nums.items():
            if freq > length//2:
                return num