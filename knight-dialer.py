class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        neighbours = {
            1:[6, 8], 
            2:[7, 9], 
            3:[4, 8],
            4:[0, 3, 9],
            5:[],
            6:[0, 1, 7],
            7:[2, 6],
            8:[1, 3],
            9:[2, 4],
            0:[4, 6]
        }

        memo = defaultdict(int, {(1, 1) : 1, (2, 1) : 1, (3, 1):1, (4, 1):1, (5, 1):1, (6, 1):1, (7, 1):1, (8, 1):1, (9, 1):1, (0, 1):1})

        res = 0
        for j in range(2, n + 1):
            for i in range(10):
                for adj in neighbours[i]:
                    memo[(i, j)] += memo[(adj, j - 1)]
                if j == n:
                    res += memo[(i, j)]

        return res % (10 ** 9 + 7)