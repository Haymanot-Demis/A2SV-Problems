class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, 0, src)]
        distance_arr = [inf] * n
        distance_arr[src] = 0
        k = k
        
        while heap:
            stops, cost, node = heappop(heap)

            if stops <= k:
                for adj, w in graph[node]:
                    if distance_arr[adj] > cost + w:
                        distance_arr[adj] = cost + w
                        heappush(heap, (stops + 1, cost + w, adj))

        return distance_arr[dst] if distance_arr[dst] != inf else -1

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         graph = defaultdict(list)
#         for start, dest, price in flights:
#             graph[start].append((dest, price))
        
#         prices = [float('inf') for i in range(n)]
#         prices[src] = 0
        
#         minHeap = [( 0, prices[src], src)]
        
#         while minHeap:
#             stops, total_cost, cur = heappop(minHeap)
#             neighbours = graph[cur]
            
#             for neighbour, cost in neighbours:
#                 if prices[neighbour] > total_cost + cost and stops <= k: 
#                     prices[neighbour] = total_cost + cost
                    
#                     heappush(minHeap, (stops + 1, prices[neighbour], neighbour))

#         return prices[dst] if prices[dst] != float('inf') else -1