#time 50
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        length = len(nums)
        maxLen = 0
        firstIndexOf = {}
        prefixsum = 0
        for i in range(0, length):
            if nums[i] == 0:
                prefixsum -= 1
            else:
                prefixsum += 1
            
            if prefixsum == 0:
               maxLen = max(maxLen, i + 1)
            elif prefixsum in firstIndexOf:
                maxLen = max(maxLen, i - firstIndexOf[prefixsum])
            else:
                firstIndexOf[prefixsum] = i           

        return maxLen