class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incomings = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            incomings[u] += 1
            incomings[v] += 1
        queue = deque()
        visited = set()
        
        for node in graph:
            if len(graph[node]) == 1:
                queue.append(node)
                visited.add(node)
        answer = [0]
        while queue:
            length = len(queue)
            answer = []
            for _ in range(length):
                curr = queue.popleft()
                answer.append(curr)
                for adj in graph[curr]:
                    incomings[adj] -= 1
                    if adj not in visited and incomings[adj] == 1:
                        queue.append(adj)
                        visited.add(adj)
            
        return answer