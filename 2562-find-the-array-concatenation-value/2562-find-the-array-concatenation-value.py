
import random 
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        conncatination_value = 0
        length = len(nums)
        right = length - 1
        left = 0
        while left < right:
            conncatination_value += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
            
        if length % 2 == 1:
            conncatination_value += int(str(nums[left]))
        return conncatination_value
            
        