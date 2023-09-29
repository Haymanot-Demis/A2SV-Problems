class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))     

        memo = [score for age, score in players]
        visited = set()

        def dp(indx, prev):
            if indx >= len(players):
                return 0
            
            if players[indx][1] < players[prev][1]:
                if indx not in visited:
                    memo[indx] += dp(indx + 1, indx)
                    visited.add(indx)

                return dp(indx + 1, prev)

            if indx not in visited:
                memo[indx] += dp(indx + 1, indx)
                visited.add(indx)
            
            return max(memo[indx], dp(indx + 1, prev))
        
        res = dp(0, 0)

        return max(memo)