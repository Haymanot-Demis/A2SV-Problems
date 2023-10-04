class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        start from the starting node go to its children, if they have better time now add it to the queue, always take the node with samllest time taken from the queue.
        '''
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        signalReachedAt = [inf] * n
        signalReachedAt[k - 1] = 0

        minheap = [(0, k)]

        while minheap:
            time, u = heappop(minheap)

            for adj in adj_list[u]:
                v, w = adj
                if signalReachedAt[v - 1] > time + w:
                    heappush(minheap, (time + w, v))
                    signalReachedAt[v - 1] = time + w

        if inf  in signalReachedAt:
            return -1

        return max(signalReachedAt)