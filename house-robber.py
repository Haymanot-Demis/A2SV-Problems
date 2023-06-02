class Solution:
    def rob(self, nums: List[int]) -> int:
        pprev, prev = 0, nums[0]

        for i in range(1, len(nums)):
            temp = prev 
            prev = max(pprev + nums[i], prev)
            pprev = temp
        
        return max(pprev, prev)