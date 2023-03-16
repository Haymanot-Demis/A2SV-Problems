class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache    
        def isWinner(l, r, turn):
            if l > r:
                return 0

            if turn:
                left = nums[l] + isWinner(l + 1, r, not turn)
                right = nums[r] + isWinner(l, r - 1, not turn)
                return max(left, right)
            else:
                left = -nums[l] + isWinner(l + 1, r, not turn)
                right = -nums[r] + isWinner(l, r - 1, not turn)
                return min(left, right)

        res = isWinner(0, len(nums) - 1, True)
        return res >=  0