class Solution: 
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = {}

        def dp(indx, last_date):
            if indx == len(days):
                return 0
            if (indx, last_date) in  memo:
                return memo[(indx, last_date)]

            if days[indx] < last_date:
                memo[(indx, last_date)] = dp(indx + 1, last_date)
                return memo[(indx, last_date)]
            
            one = dp(indx + 1, days[indx]) + costs[0]
            two = dp(indx + 1, days[indx] + 7) + costs[1]
            three = dp(indx + 1, days[indx] + 30) + costs[2]

            memo[(indx, last_date)] = min(one, two, three)
            return memo[(indx, last_date)]
        
        return dp(0, 0)