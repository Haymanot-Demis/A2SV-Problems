class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_requests = 0
        def backtrack(indx, count, net_transfer):
            nonlocal max_requests
            if indx >= len(requests):
                if net_transfer.count(0) == len(net_transfer):
                    max_requests = max(max_requests, count)
                return

            net_transfer[requests[indx][0]] -= 1
            net_transfer[requests[indx][1]] += 1 
            backtrack(indx + 1, count + 1, net_transfer)  

            net_transfer[requests[indx][0]] += 1
            net_transfer[requests[indx][1]] -= 1         
            backtrack(indx + 1, count, net_transfer)

        backtrack(0, 0, [0] * n)
        return max_requests