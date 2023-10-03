class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        prefix_sum = 0
        time_like_coef = 0
        for i, val in enumerate(satisfaction):
            if prefix_sum > -val:
                time_like_coef += prefix_sum + val
            else:
                return time_like_coef
            
            prefix_sum += val
            
        return time_like_coef