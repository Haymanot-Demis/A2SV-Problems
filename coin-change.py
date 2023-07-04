class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(lambda : inf)
        def dp(target):
            if target in memo:
                return memo[target]

            if target == amount:
                return 0

            if target > amount:
                return inf

            ans = inf
            for i in range(len(coins)):
                ans = min(ans, dp(target + coins[i]) + 1)
            memo[target] = ans
            return ans

        result = dp(0)
        if result == inf:
            return -1
        return result