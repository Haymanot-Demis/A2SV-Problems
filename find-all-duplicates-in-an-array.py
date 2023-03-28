class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        length = len(nums)
        indx = 0
        duplicates = set()
        while indx < length:
            if nums[indx] == -1:
                indx += 1
            elif nums[indx] - 1 == indx:
                nums[indx] = -1
                indx += 1
            elif nums[nums[indx] - 1] != -1:
                nums[nums[indx] - 1], nums[indx] = -1, nums[nums[indx] - 1]
            else:
                duplicates.add(nums[indx])
                indx += 1
        return duplicates