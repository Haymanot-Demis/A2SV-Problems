class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        # first add the first k points then add one card from the end of the card list and subtract on card from right side of the first k cards
        j = len(cardPoints) - 1
        currScore = sum(cardPoints[:k]) 
        maxScore = currScore
        k -= 1
        while k >= 0:
            currScore += cardPoints[j]
            currScore -= cardPoints[k]
            maxScore = max(currScore, maxScore)
            k -= 1
            j -= 1
        return maxScore
