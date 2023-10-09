class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        prob_arr = [-inf] * n
        prob_arr[start_node] = 1
        heap = [(-1, start_node)]
        processed = set()

        while heap:
            prob, node = heappop(heap)
            prob = prob_arr[node]

            # if node in processed:
            #     continue
            
            processed.add(node)

            for adj, p in graph[node]:
                if prob_arr[adj] < prob * p: 
                    prob_arr[adj] = prob * p
                    heappush(heap, (-prob_arr[adj], adj))
        
        return 0 if prob_arr[end_node] == -inf else prob_arr[end_node]