class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        memo = defaultdict(bool)

        def dp(indx):
            if indx in memo:
                return memo[indx]
            
            if indx >= len(nums):
                return True
            
            if indx == len(nums) - 1:
                memo[indx] = False
                return False

            memo[indx] = False

            # checking for condition one or three
            if len(nums) >= indx + 3:
                if (nums[indx] == nums[indx + 1] - 1 and nums[indx + 1] == nums[indx + 2] - 1) or (nums[indx] == nums[indx + 1] == nums[indx + 2]):
                    memo[indx] = dp(indx + 3)

            # checking for condition 2
            if nums[indx] == nums[indx + 1]:
                memo[indx] |= dp(indx + 2)
            
            return memo[indx]                
        
        return dp(0)