class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        return self.help(nums, 0, 0, 0, memo)

    def help(self, nums, indx, sum1, sum2, memo):
        if indx == len(nums):
            if sum1 == sum2:
                return True
            return False
        
        if (sum1, sum2, indx)  in memo:
            return memo[(sum1, sum2, indx)]
        res1 = self.help(nums, indx + 1, sum1 + nums[indx], sum2, memo)
        if res1:
            return True
        res2 = self.help(nums, indx + 1, sum1, sum2 + nums[indx], memo)
        memo[(sum1, sum2, indx)] = res2

        return res2