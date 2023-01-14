from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, loosers = list(zip(*matches))
        winnersHash, loosersHash = Counter(winners), Counter(loosers)         
        return [sorted([winnes for winnes in winnersHash.keys() if winnes not in loosersHash]), sorted([player for player, lose in loosersHash.items() if lose == 1])]