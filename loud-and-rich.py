class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        
        peoples = graph.keys()
        answer = [-1] * len(quiet)
        for rich in range(len(quiet)):
            self.dfs(graph, rich, quiet, answer)

        return answer

    def dfs(self, graph, rich, quiet, answer):
        if answer[rich] != -1:
            return answer[rich]

        if rich not in graph:
            answer[rich] = rich
            return rich
            
        least_quiet = rich
        for adj in graph[rich]:
            ans = self.dfs(graph, adj, quiet, answer)
            if quiet[ans] <= quiet[least_quiet]:
                least_quiet = ans
        
        answer[rich] = least_quiet
        return least_quiet