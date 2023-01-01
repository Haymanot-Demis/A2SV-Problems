class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        right = 0
        count = 0
        maxCount = 0
        deletedIndx = -1
        length = len(nums)
        while right < length and nums[right] != 1:
            right += 1
        
        while right < length:
            if nums[right] == 1:
                count += 1
            elif nums[right] == 0:
                if deletedIndx >= 0:
                    maxCount = max(maxCount, count)
                    count = right - deletedIndx - 1
                    deletedIndx = right
                    if count == 0:
                        deletedIndx = -1
                        while right < length and nums[right] != 1:
                            right += 1
                        right -= 1
                else:
                    deletedIndx = right
            right += 1
        print(count)
        maxCount = max(maxCount, count)

        return maxCount if maxCount < length else maxCount - 1