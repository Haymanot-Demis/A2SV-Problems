# this is a perfect solution for finding a minimal subarray whose sum is equal to target
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        right = 0
        minLength = len(nums) + 1
        minSubarray = []
        sum = nums[0]
        while right < len(nums) and left <= right:
            subarray = nums[left:right+1]
            if sum >= target:
                if minLength > len(subarray):
                    minLength = len(subarray)
                    minSubarray = subarray
                sum -= nums[left]
                left += 1
                continue
            else:
                right += 1
                if right < len(nums):
                    sum += nums[right]
            

        print(minSubarray)
        if minLength == len(nums) + 1:
            return 0
        return minLength
                            


