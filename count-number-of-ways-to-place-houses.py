class Solution:
    def countHousePlacements(self, n: int) -> int:
        memo = [0] * max(2, n)
        memo[0] = 2
        memo[1] = 3

        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]

        return (memo[n - 1] * memo[n - 1]) % (10 ** 9 + 7)