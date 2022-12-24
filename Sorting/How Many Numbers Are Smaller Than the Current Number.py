class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
       numCopy = nums.copy()
       numCopy.sort()

       return [numCopy.index(num) for num in nums]