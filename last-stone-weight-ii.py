class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        memo = {}
        
        def dp(target, idx, num):
            
            if idx >= len(stones):
                return num
            
            elif (idx, num) in memo:
                return memo[(idx, num)]
            
            if stones[idx] + num > target:
                memo[(idx, num)] =  dp(target, idx+1, num)
            else:
                memo[(idx, num)] = max(dp(target, idx+1, num+stones[idx]), dp(target, idx+1, num))
            
            return memo[(idx, num)]
        
        target = math.ceil(sum(stones) / 2)
        
        return abs(sum(stones) - 2*(dp(target, 0, 0)))