class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        right = [0] * len(rating)
        left = [0] * len(rating)
        
        teams = 0
        
        for i in range(len(rating)-1, -1, -1):
            for j in range(i+1, len(rating)):
                if rating[i] < rating[j]:
                    right[i] += 1
                    teams += right[j]
                else:
                    left[i] += 1
                    teams += left[j]
        
        return teams