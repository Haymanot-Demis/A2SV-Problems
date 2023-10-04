class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        node_freq = defaultdict(int)
        adj_list = defaultdict(list)
        score = 0

        for u, v in edges:
            adj_list[u].append(v)        
            adj_list[v].append(u)

        score = self.getScore(adj_list, trips, node_freq, price)
        memo = defaultdict(int)

        def dp(node, parent, color):
            if (node, color) in memo:
                return memo[(node, color)]
                
            if color == 1:
                discount = (node_freq[node]) * (price[node] // 2)
                for adj in adj_list[node]:
                    if adj != parent:
                        discount += dp(adj, node, not color)
            else:
                discount = 0
                for adj in adj_list[node]:
                    if adj != parent:
                        one = dp(adj, node, color)
                        two = dp(adj, node, not color)
                        discount += max(one, two)
            memo[(node, color)] = discount
            return discount

        res = max(dp(0, None, 0), dp(0, None, 1))
        
        return score - res

    def getScore(self, adj_list, trips, node_freq, price):
        score = 0
        def traverseTrip(node, parent, end, path):
            path[node] = parent
            if node == end:
                return
            for adj in adj_list[node]:
                if adj != parent:
                    traverseTrip(adj, node, end, path)
        
        for start, end in trips:
            path = {}
            traverseTrip(start, None, end, path)
            n = end
            while n != None:
                node_freq[n] += 1
                n = path[n]

        for n, freq in node_freq.items():
            score += price[n] * freq
        
        return score