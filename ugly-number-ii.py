class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        ugly = []
        visited = set()
        while len(ugly) < n:
            small = heappop(heap)
            for prime in [2, 3, 5]:
                nxt = small * prime
                if nxt not in visited:
                    heappush(heap, nxt)
                    visited.add(nxt)
            ugly.append(small)
        
        return ugly[-1]