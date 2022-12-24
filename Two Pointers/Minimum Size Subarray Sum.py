class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        right = 0
        numsLength = len(nums)
        minLength = numsLength  + 1
        # minSubarray = []
        sum = nums[0]
        while right < len(nums) and left <= right:
            # subarray = nums[left:right+1]
            if sum >= target:
                if minLength > right - left + 1:
                    minLength = right - left + 1
                    # minLength = len(subarray)
                    # minSubarray = subarray
                sum -= nums[left]
                left += 1
                continue
            else:
                right += 1
                if right < len(nums):
                    sum += nums[right]
            

        # print(minSubarray)
        if minLength == numsLength + 1:
            return 0
        return minLength
                          