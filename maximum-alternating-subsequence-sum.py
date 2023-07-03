class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        memo = {}

        def dp(indx, parity):
            # parity = True for even, False for odd
            # if even we will add else we will subtract the current number
            if indx == len(nums):
                return 0
            
            if (indx, parity) in memo:
                return memo[(indx, parity)]
            # if we take the current number
            if parity:
                one = nums[indx] + dp(indx + 1, not parity)
            else:
                one = -nums[indx] + dp(indx + 1, not parity)
            
            # if leave the current number
            two = dp(indx + 1, parity)

            memo[(indx, parity)] = max(one, two)

            return memo[(indx, parity)]

        return dp(0, True)