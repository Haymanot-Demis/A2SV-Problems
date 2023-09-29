class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        think about minimum initial health needed to rescue the princess starting from the current cell
        """

        memo = defaultdict(lambda : inf)
        m = len(dungeon)
        n = len(dungeon[0])
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) == (m - 1, n - 1):
                    if dungeon[i][j] < 0:
                        memo[(i, j)] = abs(dungeon[i][j] - 1)
                    else:
                        memo[(i, j)] = 1
                    continue

                right = memo[(i, j + 1)]
                down = memo[(i + 1, j)]

                nxt = min(right, down)

                if dungeon[i][j] < 0:
                    curr = nxt + abs(dungeon[i][j])
                else:
                    if nxt <= dungeon[i][j]:
                        curr = 1
                    else:
                        curr = nxt - dungeon[i][j]

                memo[(i, j)] = curr 
                
        return memo[(0, 0)]