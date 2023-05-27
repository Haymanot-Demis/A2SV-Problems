class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        i = 0
        for costA, costB in costs:
            diff.append((costA - costB, i))
            i += 1
        
        diff.sort()
        min_cost = 0
        for i in range(len(costs) // 2):
            min_cost += costs[diff[i][1]][0]

        for i in range(len(costs) // 2, len(costs)):
            min_cost += costs[diff[i][1]][1]
        
        return min_cost