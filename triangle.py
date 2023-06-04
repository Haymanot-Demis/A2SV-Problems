class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [ [inf] * len(row) for row in triangle ]
        memo[0][0] = triangle[0][0]

        for level in range(len(triangle) - 1):
            for indx in range(len(triangle[level])):

                prev = memo[level + 1][indx]
                new = memo[level][indx] + triangle[level + 1][indx]
                memo[level + 1][indx] = min(prev, new)

                prev = memo[level + 1][indx + 1]
                new = memo[level][indx] + triangle[level + 1][indx + 1]
                memo[level + 1][indx + 1] = min(prev, new)
    
        return min(memo[-1])