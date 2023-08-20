class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        memo = defaultdict(lambda : -inf)

        @cache
        def dp(indx):
            if indx == len(nums) - 1:
                return 1
            
            if indx >= len(nums):
                return -inf
            
            # if indx in memo:
            #     return memo[indx]
            
            for j in range(indx + 1, len(nums)):
                if -target <= nums[j] - nums[indx] <= target:
                    memo[indx] = max(memo[indx], dp(j))
            return memo[indx] + 1
        
        dp(0)
        if memo[0] == -inf:
            return -1
        return memo[0]