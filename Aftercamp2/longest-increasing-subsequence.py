class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = defaultdict(lambda : 1)

        def dp(indx):
            if indx == len(nums):
                return 0
            if indx in memo:
                return memo[indx]
            
            for j in range(indx + 1, len(nums)):
                if nums[indx] < nums[j]:
                    memo[indx] = max(memo[indx], dp(j) + 1)

            return memo[indx]

        for i in range(len(nums)):
            dp(i)
        return max(memo.values())      
            