class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for parent, child in edges:
            graph[child].append(parent)

        visited = set()

        answer = [set() for _ in range(n)]
        
        for node in range(n):
            if node in graph and node not in visited:
                self.dfs(graph, node, visited, answer)
        
        for indx, ancestors in enumerate(answer):
            answer[indx] = sorted(ancestors)

        return answer
    def dfs(self, graph, node, visited, answer):
        visited.add(node)
        ancestors = set()

        for ancestor in graph[node]:
            if ancestor not in visited:
                result = self.dfs(graph, ancestor, visited, answer)
                ancestors |= result
            else:
                ancestors |= answer[ancestor] | set([ancestor]) 
        answer[node] |= ancestors

        return ancestors | set([node])