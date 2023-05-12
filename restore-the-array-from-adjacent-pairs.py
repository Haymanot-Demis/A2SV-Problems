class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incomings = defaultdict(int)

        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque()
        for node, adjacents in graph.items():
            incomings[node] = len(adjacents)
            if len(adjacents) == 1:
                queue.append(node)

        nums = []
        queue = deque([queue[0]])
        visited = set()
        
        while queue:
            curr = queue.popleft()
            nums.append(curr)
            visited.add(curr)
            for adj in graph[curr]:
                incomings[adj] -= 1
                if adj not in visited and incomings[adj] <= 1:
                    queue.append(adj)
        
        return nums