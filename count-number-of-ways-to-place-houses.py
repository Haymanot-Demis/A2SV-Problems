class Solution:
    def countHousePlacements(self, n: int) -> int:
        if n == 1:
            return 4
        
        if n == 2:
            return 9

        pprev = 2
        prev = 3
        modulo = 10 ** 9 + 7

        for i in range(2, n):
            prev += pprev
            pprev = prev - pprev

        return (prev * prev) % modulo