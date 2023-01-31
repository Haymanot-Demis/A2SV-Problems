#time = 15
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        l1 = len(players) - 1
        l2 = len(trainers) - 1
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        count = 0
        while l1 > -1 and l2 > -1:
            if players[l1] <= trainers[l2]:
                count += 1
                l1 -= 1
            l2 -= 1
        return count