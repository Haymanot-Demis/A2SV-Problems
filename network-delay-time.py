class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        memo = [inf] * n
        def minTimeToSignal(node, time):
            if memo[node - 1] <= time:
                return 
            memo[node - 1] = time
            for adj in adj_list[node]:
                v, w = adj
                minTimeToSignal(v, time + w)

            return
        minTimeToSignal(k, 0)

        if inf  in memo:
            return -1

        return max(memo)