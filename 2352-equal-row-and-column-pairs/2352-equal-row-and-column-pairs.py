import json, collections
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = collections.defaultdict(int)
        length = len(grid)
        cols = []
        count = 0
        for i in range(length):
            rows[json.dumps(grid[i])] += 1
        for col in range(length):
            column = []
            for row in range(length):
                column.append(grid[row][col])
            dumped = json.dumps(column)
            if rows.get(dumped,-1) != -1:
                count += rows [dumped]   
        
        return count
