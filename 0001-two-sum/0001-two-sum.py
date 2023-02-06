class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(list(enumerate(nums)), key = lambda x : x[1])
        length = len(nums)
        left = 0
        right = length - 1
        while left < right:
            if nums[right][1] + nums[left][1] > target:
               right -= 1
            elif nums[right][1] + nums[left][1] < target:
                left += 1
            else:
                return [nums[right][0], nums[left][0]]

            