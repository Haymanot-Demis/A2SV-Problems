class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        #I think we have to test every path in which the first person can go through
        first, second = self.IsWinner(nums, 0, len(nums) - 1, 0, 0, True)
        return first >=  second

    def IsWinner(self, nums, l, r, first, second, turn):
        if r < l:
            return [first, second]
        if turn:
            f1,s1 = self.IsWinner(nums, l+1, r, first + nums[l], second, not turn)
            f2,s2 = self.IsWinner(nums, l, r - 1, first + nums[r], second, not turn)
            if f1 >= f2:
                return [f1, s1]
            else:
                return [f2, s2]
        else:
            f1,s1 = self.IsWinner(nums, l+1, r, first, second + nums[l], not turn)
            f2,s2 = self.IsWinner(nums, l, r - 1, first, second + nums[r], not turn)
            if s1 >= s2:
                return [f1, s1]
            else:
                return [f2, s2]