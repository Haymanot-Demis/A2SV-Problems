class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if 2 * candidates >= len(costs):
            costs.sort()
            return sum(costs[:k])
        else:
            left_heap = costs[:candidates]
            right_heap = costs[-candidates:]
        
            heapify(left_heap)
            heapify(right_heap)

            cost = 0
            left = candidates
            right = len(costs) - candidates - 1

            while  left <= right and k: 
                if left_heap[0] <= right_heap[0]:
                    cost += heappop(left_heap)
                    heappush(left_heap, costs[left])
                    left += 1
                else:
                    cost += heappop(right_heap)
                    heappush(right_heap, costs[right])
                    right -= 1
                k -= 1
            
            heap = left_heap + right_heap
            heapify(heap)
            
            while k > 0:
                cost += heappop(heap)
                k -= 1

            return cost