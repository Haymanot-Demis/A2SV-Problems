class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))     

        memo = [score for age, score in players]
        for i in range(len(players)):
            max_score = 0
            for j in range(i):
                if players[i][1] >= players[j][1]:
                    print(j)
                    max_score = max(max_score, memo[j])
            
            memo[i] += max_score

        return max(memo)