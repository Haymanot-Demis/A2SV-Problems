class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # bottom up approach
        
        memo = [ [0 for j in range(i + 1)] for i in range(query_row + 1)]
        memo[0][0] = poured

        for i in range(1, query_row + 1):
            for j in range(i + 1):
                if j == 0:
                    overflow = (memo[i - 1][j] - 1) / 2
                    memo[i][j] = max(0, overflow)
                elif i == j:
                    overflow = (memo[i - 1][j - 1] - 1) / 2
                    memo[i][j] = max(0, overflow)
                else:
                    overflow1 = max(0, (memo[i - 1][j - 1] - 1) / 2)
                    overflow2 = max(0, (memo[i - 1][j] - 1) / 2)
                    memo[i][j] = overflow1 + overflow2
                
        res = memo[query_row][query_glass]
        if res < 1:
            return res
        return 1



        # top down approach
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