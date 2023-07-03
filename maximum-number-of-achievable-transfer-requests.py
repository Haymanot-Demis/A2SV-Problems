class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def backtrack(indx, count, net_transfer):
            if indx >= len(requests):
                if net_transfer.count(0) == len(net_transfer):
                    return 0
                return -inf

            net_transfer[requests[indx][0]] -= 1
            net_transfer[requests[indx][1]] += 1
            one = backtrack(indx + 1, count + 1, net_transfer)  

            net_transfer[requests[indx][0]] += 1
            net_transfer[requests[indx][1]] -= 1         
            two = backtrack(indx + 1, count, net_transfer)

            return max(one + 1, two)

        return backtrack(0, 0, [0] * n)