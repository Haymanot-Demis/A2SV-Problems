class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        max_robots = 0
        maxheap = []
        run_cost_sum = 0

        left = 0
        for i in range(len(chargeTimes)):
            heappush(maxheap, (-chargeTimes[i], i))
            run_cost_sum += runningCosts[i]
            max_charge = -maxheap[0][0] if maxheap else 0

            while left <= i and max_charge  + ((i - left + 1) * run_cost_sum) > budget:
                run_cost_sum -= runningCosts[left]
                while maxheap and maxheap[0][1] <= left:
                    heappop(maxheap)

                left += 1

                if maxheap:
                    max_charge = -maxheap[0][0]
                else:
                    max_charge = 0
                
            max_robots = max(max_robots, i - left + 1)

        return max_robots