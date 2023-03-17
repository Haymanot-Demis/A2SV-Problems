class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        minimum_unfairness = float("inf")
        distribution = [0] * k
        def backtrack(indx, current_distrn):
            nonlocal minimum_unfairness
            if indx == len(cookies):
                minimum_unfairness = min(max(current_distrn), minimum_unfairness)
                return
            if max(current_distrn) >= minimum_unfairness:
                return
            for j in range(k):
                distribution[j] += cookies[indx]
                backtrack(indx + 1, distribution.copy())
                distribution[j] -= cookies[indx]
            
        backtrack(0, distribution)
        return minimum_unfairness