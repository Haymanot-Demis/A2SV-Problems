class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        res = self.backtrack(nums, 0, 0, memo, [], False)
        return res

    def backtrack(self, nums, indx, money, memo, store, flag=False):
        if indx >= len(nums):
            return money
        
        if indx == len(nums) - 1 and flag:
            return money
        
        if (indx, flag, money) not in memo:
            if indx == 0:
                m1 = self.backtrack(nums, indx + 2, money + nums[indx], memo, store + [nums[indx]],True)
            else:
                m1 = self.backtrack(nums, indx + 2, money + nums[indx], memo, store + [nums[indx]],flag)
            m2 = self.backtrack(nums, indx + 1, money, memo, store,flag)
            memo[(indx, flag, money)] = max(m1, m2)
        
        return memo[(indx, flag, money)]