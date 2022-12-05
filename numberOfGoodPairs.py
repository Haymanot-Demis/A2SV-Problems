#time = 10
import math
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        numberOfGoodPairs = 0;
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    numberOfGoodPairs += 1
        return numberOfGoodPairs

class Solution1:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        frequencyArray = [0]*100
        numberOfGoodPairs = 0;
        for num in nums:
            frequencyArray[num] += 1
   
        for item in frequencyArray:
            if item > 1:
                numberOfGoodPairs += math.factorial(item)/(math.factorial(item - 2)*math.factorial(2))
        return int(numberOfGoodPairs)

mySolution = Solution()
mySolution.numIdenticalPairs([1,2,3,1,1,3])