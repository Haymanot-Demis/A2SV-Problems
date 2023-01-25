class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countArray = [0, 0, 0]
        for num in nums:
            countArray[num] += 1
        i = 0
        for j in range(3):
            for _ in range(countArray[j]):
                nums[i] = j
                i += 1
