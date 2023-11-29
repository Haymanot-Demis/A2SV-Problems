import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numberOfGoodPairs = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    numberOfGoodPairs += 1
        return numberOfGoodPairs