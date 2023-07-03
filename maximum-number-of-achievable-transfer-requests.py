class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def backtrack(indx, net_transfer, memo):
            if indx >= len(requests):
                if net_transfer.count(0) == len(net_transfer):
                    return 0
                return -inf
            
            if (indx, net_transfer) in memo:
                return memo[(indx, net_transfer)]
        
            net_transfer1 = list(net_transfer)
            net_transfer1[requests[indx][0]] -= 1
            net_transfer1[requests[indx][1]] += 1

            one = backtrack(indx + 1, tuple(net_transfer1), memo)  
            two = backtrack(indx + 1, net_transfer, memo)

            memo[(indx, net_transfer)] = max(one + 1, two)

            return max(one + 1, two)

        return backtrack(0, tuple([0] * n), defaultdict(int))