class Solution:
    def maxNonOverlapping(self, nums: list[int], target: int) -> int:
        hashmap = dict()
        lastSubArrIndx = -1
        counter = 0
        hashmap[nums[0]] = 0

        if nums[0] == target:
            lastSubArrIndx = 0
            counter += 1
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i] == target and lastSubArrIndx == -1:
                counter += 1
                lastSubArrIndx = i
            elif hashmap.get(nums[i] - target, -2) >= lastSubArrIndx:
                counter += 1
                lastSubArrIndx = i
            hashmap[nums[i]] = i
        return counter