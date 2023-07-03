class Solution:
    def countHousePlacements(self, n: int) -> int:
        pprev = 1
        prev = 2
        modulo = 10 ** 9 + 7

        for i in range(1, n):
            prev += pprev
            pprev = prev - pprev

        return (prev * prev) % modulo