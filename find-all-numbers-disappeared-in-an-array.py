class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        indx = 0
        disappeared = []
        while indx < length:
            if nums[indx] - 1 == indx:
                nums[indx] = -1
                indx += 1
            elif nums[indx] != -1 and nums[nums[indx] - 1] != -1:
                nums[nums[indx] - 1], nums[indx] = -1, nums[nums[indx] - 1]
            else:
                indx += 1
        
        for indx in range(length):
            if nums[indx] != -1:
                disappeared.append(indx + 1)
        return disappeared

        return duplicates