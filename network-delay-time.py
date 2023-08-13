class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        signalReachedAt = [inf] * n
        signalReachedAt[k - 1] = 0

        queue = deque([(k, 0)])

        while queue:
            u, time = queue.popleft()

            for adj in adj_list[u]:
                v, w = adj
                if signalReachedAt[v - 1] > time + w:
                    queue.append((v , time + w))
                    signalReachedAt[v - 1] = time + w
        
        if inf  in signalReachedAt:
            return -1

        return max(signalReachedAt)