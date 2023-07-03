class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even, odd = 0, nums[0]

        for i in range(len(nums)):
            even = max(even, odd - nums[i])
            odd = max(odd, even + nums[i])

        return max(even, odd)