class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse_graph = defaultdict(list)
        outgoing = defaultdict(int)

        for node, destinations in enumerate(graph):
            for dest in destinations:
                reverse_graph[dest].append(node)
            outgoing[node] += len(destinations)
        
        queue = deque()

        for node in range(len(graph)):
            if outgoing[node] == 0:
                queue.append(node)
            
        answer = []
        print(queue)
        while queue:
            curr = queue.popleft()
            answer.append(curr)
            for source in reverse_graph[curr]:
                outgoing[source] -= 1
                if outgoing[source] == 0:
                    queue.append(source)
        
        return sorted(answer)