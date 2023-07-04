class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        return self.help(nums, 0, 0, memo)

    def help(self, nums, indx, target, memo):
        if indx == len(nums):
            if target == 0:
                return True
            return False
        
        if (target, indx)  in memo:
            return memo[(target, indx)]

        if (target, indx) in memo:
            return memo[(target, indx)]

        res1 = self.help(nums, indx + 1, target + nums[indx], memo)
        if res1:
            return True
        res2 = self.help(nums, indx + 1, target - nums[indx], memo)
        memo[(target, indx)] = res2

        return res2