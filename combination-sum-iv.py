class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.backtrack(nums, 0, 0, [], target, {})
    def backtrack(self, nums, indx, sums, mems, target, memo):
        if sums == target:
            return 1
        if indx >= len(nums):
            return 0
        
        if sums > target:
            return 0
        if (indx, sums) not in memo:
            valids = 0
            for i in range(len(nums)):
                valids += self.backtrack(nums, i, sums + nums[i], mems + [nums[i]], target, memo)
            memo[(indx, sums)] = valids
        return memo[(indx, sums)]