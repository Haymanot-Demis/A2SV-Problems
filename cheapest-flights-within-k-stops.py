class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        queue = deque([(0, src)])
        distance_arr = [inf] * n  
        distance_arr[src] = 0   
        k = k + 1

        while k:
            length = len(queue)

            for _ in range(length):
                cost, node = queue.popleft()  

                for adj, w in graph[node]:
                    if distance_arr[adj] > cost + w:
                        distance_arr[adj] = cost + w
                        queue.append((cost + w, adj))  
            k -= 1
        
        if distance_arr[dst] == inf:
            return -1
        return distance_arr[dst]