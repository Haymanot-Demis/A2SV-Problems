class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        min_max = sum(nums)
        ans = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            ans = max(ans, -(-(total) // (i + 1)))
            
        return ans