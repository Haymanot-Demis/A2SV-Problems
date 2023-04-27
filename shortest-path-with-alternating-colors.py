class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for source, dest in redEdges:
            adj_list[source].append((dest, "r"))
        
        for source, dest in blueEdges:
            adj_list[source].append((dest, "b"))
        
        queue = deque([(0, 0,"None")])
        visited = set()
        answer = [-1] * n

        while queue:
            length = len(queue)
            curr_node, path_len, color = queue.popleft()
            if answer[curr_node] == -1:
                answer[curr_node] = path_len
            for adj in adj_list[curr_node]:
                    if adj not in visited and color != adj[1]:
                        queue.append((adj[0], path_len + 1, adj[1]))
                        visited.add(adj)
        return answer