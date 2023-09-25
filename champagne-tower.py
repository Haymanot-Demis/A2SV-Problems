class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = defaultdict(int, {(0, 0) : max(0, poured)})
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == 0:
                overflow = (dp(i - 1, j) - 1) / 2
                memo[(i, j)] = max(0, overflow)
            elif j == i:
                overflow = (dp(i - 1, j - 1) - 1) / 2
                memo[(i, j)] =  max(0, overflow)
            else:
                overflow1 = max(0, (dp(i - 1, j - 1) - 1) / 2)
                overflow2 = max(0, (dp(i - 1, j) - 1) / 2)
                overflow = overflow1 + overflow2
                memo[(i, j)] = max(0, overflow)
            
            return memo[(i, j)]
        
        res = dp(query_row, query_glass)
       
        if res < 1:
            return res
        return 1.000