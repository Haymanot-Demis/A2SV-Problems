#60
from collections import defaultdict 
class Solution:
    def maxOperations_2(self, nums: list[int], k: int) -> int: # this has high running time when the array becomes very huge in size
        num = len(nums)
        i = 0
        counter = 0
        while i < num:
            currNum = nums[i]
            copyList = nums.copy()
            copyList.remove(currNum)
            if k - currNum in copyList:
                nums.remove(k - currNum)
                nums.remove(currNum)
                num = len(nums)
                counter += 1
            else:
                i += 1
        return counter

    class Solution:
        def maxOperations(self, nums: list[int], k: int) -> int:
            counterDictionary = defaultdict(int)
            num_of_pairs = 0
            for num in nums:
                if counterDictionary[num] > 0:
                    counterDictionary[num]-=1
                    num_of_pairs+=1
                else:
                    counterDictionary[k-num]+=1
            
            return num_of_pairs

