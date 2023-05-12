class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incomings = defaultdict(int)

        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque()
        for node, adjacents in graph.items():
            if len(adjacents) == 1:
                queue.append(node)
                break

        nums = []
        visited = set()

        while queue:
            curr = queue.popleft()
            nums.append(curr)
            for adj in graph[curr]:
                graph[curr].remove(adj)
                graph[adj].remove(curr)
                queue.append(adj)
        
        return nums