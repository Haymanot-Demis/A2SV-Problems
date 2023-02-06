class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for indx, num in enumerate(nums):
            if target - num in hashTable:
                return [indx, hashTable[target - num]]
            else:
                hashTable[num] = indx
            