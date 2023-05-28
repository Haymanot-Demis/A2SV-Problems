class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0:cost[0], 1:cost[1]}
        self.minCost(cost, len(cost) - 1, memo)

        return min(memo[len(cost) - 1], memo[len(cost) - 2])

    def minCost(self, cost, pos, memo):
        if pos in memo:
            return memo[pos]
        way1 = self.minCost(cost, pos - 1, memo)
        way2 = self.minCost(cost, pos - 2, memo)
        memo[pos] = min(way1, way2) + cost[pos]
        return memo[pos]