from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnersHash = defaultdict(int)
        loosersHash = defaultdict(int)
        for match in matches:
            winnersHash[match[0]] += 1
            loosersHash[match[1]] += 1
        return [sorted([winnes for winnes in winnersHash.keys() if winnes not in loosersHash]), sorted([player for player, lose in loosersHash.items() if lose == 1])]