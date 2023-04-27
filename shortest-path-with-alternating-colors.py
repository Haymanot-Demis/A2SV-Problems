class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for source, dest in redEdges:
            adj_list[source].append((dest, "r"))
        
        for source, dest in blueEdges:
            adj_list[source].append((dest, "b"))
        
        queue = deque([(0, "b"), (0, "r")])
        visited = set()
        shortest_path = -1
        answer = [-1] * n

        while queue:
            shortest_path += 1
            length = len(queue)
            for i in range(length):
                curr_node, color = queue.popleft()
                if answer[curr_node] == -1:
                    answer[curr_node] = shortest_path
                for adj in adj_list[curr_node]:
                    if adj not in visited and color != adj[1]:
                        queue.append(adj)
                        visited.add(adj)
        return answer