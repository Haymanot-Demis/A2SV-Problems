class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
      def solution():
        if sum(gas) < sum(cost):
          return -1

        total = 0
        size = len(gas)
        start = 0
        for i in range(size):
          total += gas[i] - cost[i]

          if total < 0:
            total = 0
            start = i + 1
        return start
      
      return solution()

        