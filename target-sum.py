class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        return self.backtrack(nums, 0, target, memo)
    
    def backtrack(self, nums, indx, target, memo):
        if indx >= len(nums):
            return target == 0
        
        if (target, indx) in memo:
            return memo[(target, indx)]
        
        valids = 0
        res = self.backtrack(nums, indx + 1, target + nums[indx], memo)        
        if res:
            valids += res
        res = self.backtrack(nums, indx + 1, target - nums[indx], memo)
        if res:
            valids += res
        memo[(target, indx)] = valids
        return valids