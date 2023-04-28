class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        self.dfs(graph, 0, len(graph) - 1, [], paths)

        return paths

    def dfs(self, graph, node, dest, path, paths):
        if node == dest:
            paths.append(path + [node])

        for adj in graph[node]:
            self.dfs(graph, adj, dest, path + [node], paths)