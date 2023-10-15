class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = defaultdict(int)

        def dp(indx, steps):
            inbound = 0 <= indx < arrLen

            if not inbound:
                return 0
            
            if indx == 0 and steps == 0:
                return 1
            
            if inbound and steps == 0:
                return 0

            if (indx, steps)  in memo:
                return memo[(indx, steps)]

            ways = 0
          
            ways +=  dp(indx + 1, steps - 1)  
            ways +=  dp(indx, steps - 1)  
            ways +=  dp(indx - 1, steps - 1)

            memo[(indx, steps)] = ways
            return ways

        return dp(0, steps) % (10 ** 9 + 7)