class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        answer = [0] * n
        answer[0] = 1
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        nodes = list(graph.keys())
        visited = set()

        for node in nodes:
            if node not in visited:
                self.dfs(graph, 0, answer, labels, visited)

        return answer
    
    def cancatinateDict(self, dict1, dict2):
        merged = defaultdict(int)
        for key, value in dict1.items():
            merged[key] = value + dict2[key]
        for key, value in dict2.items():
            if key not in dict1:
                merged[key] += value

        return merged
    
    def dfs(self, graph, node, answer, labels, visited):
        same_labels = defaultdict(int, {labels[node]:1})
        visited.add(node)
        for adj in graph[node]:
            if adj not in visited:
                res = self.dfs(graph, adj, answer, labels, visited)
                same_labels = self.cancatinateDict(res, same_labels)

        answer[node] = same_labels[labels[node]]
        return same_labels