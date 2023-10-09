class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        weights = {}
        nodes = set()
        for i, (u, v) in enumerate(equations):
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))
            nodes.add(u)
            nodes.add(v)
        
        def BFS(src, end):
            if src not in nodes or end not in nodes:
                return -1
            
            if src == end:
                return 1

            queue = deque([(src, 1)])
            visited = set([src])
            path = {src:None}

            while queue:
                length = len(queue)

                for _ in range(length):
                    curr, c = queue.popleft()

                    for adj, w in graph[curr]:
                        if adj not in visited:
                            queue.append((adj, c * w))
                            visited.add(adj)

                            if adj == end:
                                return c * w
            return -1
        answer = []
        for s, d in queries:
            answer.append(BFS(s, d))

        return answer