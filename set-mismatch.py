class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pointer = 0
        duplicated = None

        while pointer < length:
            if nums[pointer] == -1:
                pointer += 1
            elif nums[pointer] - 1 == pointer:
                nums[pointer] = -1
                pointer += 1
            elif nums[nums[pointer] - 1] != -1:
               nums[nums[pointer] - 1], nums[pointer] = -1, nums[nums[pointer] - 1]
            else:
                duplicated = nums[pointer]
                pointer += 1
        print(nums)
        for i in range(length):
            if nums[i] != -1:
                return [duplicated, i + 1]
        return [duplicated, length]