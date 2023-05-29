class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.backtrack(nums, 0, memo)

    def backtrack(self, nums, indx, memo):
        if indx >= len(nums):
            return 0
        if indx not in memo:
            m1 = self.backtrack(nums, indx + 2, memo) + nums[indx]
            m2 = self.backtrack(nums, indx + 1, memo)
            memo[indx] = max(m1, m2)
        return memo[indx]