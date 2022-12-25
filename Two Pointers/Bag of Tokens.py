#time 33
class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        left = 0 
        right = len(tokens) - 1
        score = 0
        tokens.sort()
        while left <= right:
            if tokens[left] <= power:
                score += 1
                power -= tokens[left]
                left += 1
            elif score > 0 and left < right:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
        return score