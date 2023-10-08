class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, src)]
        distance_arr = [inf] * n  
        distance_arr[src] = 0   
        k = k + 1
        print(graph)

        while heap and k:
            length = len(heap)
            next_level = []

            for _ in range(length):
                cost, node = heappop(heap)  

                for adj, w in graph[node]:
                    if distance_arr[adj] > cost + w:
                        distance_arr[adj] = cost + w
                        next_level.append((cost + w, adj))
                    
            for nxt in next_level:
                heappush(heap, nxt)
                    
            k -= 1
        print(distance_arr)
        
        if distance_arr[dst] == inf:
            return -1
        return distance_arr[dst]