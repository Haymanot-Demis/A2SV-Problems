from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = defaultdict(int)
        hashmap[nums[0]] = 1
        counter = 0
        if nums[0] == goal:
            counter += 1
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i] == goal:
                counter += 1
            if hashmap[nums[i] - goal] != 0:
                counter += hashmap[nums[i] - goal]
            hashmap[nums[i]] += 1
        return counter