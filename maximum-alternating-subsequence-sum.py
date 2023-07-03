class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        memo = [0] * len(nums)

        even, odd = 0, nums[0]

        for i in range(len(nums)):
            memo[i] = max(even + nums[i], odd - nums[i], odd)
            even = max(even, odd - nums[i])
            odd = max(odd, even + nums[i])

        return memo[-1]