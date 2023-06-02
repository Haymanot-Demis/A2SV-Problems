class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        one = self.dp(nums[:-1])
        two = self.dp(nums[1:])

        return max(one, two)  

    def dp(self, nums):
        pprev, prev = 0, nums[0]

        for i in range(1, len(nums)):
            temp = prev 
            prev = max(pprev + nums[i], prev)
            pprev = temp
        
        return prev