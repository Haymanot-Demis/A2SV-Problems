import collections
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = collections.defaultdict(int)
        length = len(grid)
        cols = []
        count = 0
        for i in range(length):
            rows[tuple(grid[i])] += 1
        for col in range(length):
            column = []
            for row in range(length):
                column.append(grid[row][col])
            column = tuple(column)
            if rows.get(column,-1) != -1:
                count += rows [column]   
        
        return count
