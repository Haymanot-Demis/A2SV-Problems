class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLength = len(nums)
        copy = nums.copy()
        for indx in range(numsLength):
            nums[(indx + k) % numsLength] = copy[indx]