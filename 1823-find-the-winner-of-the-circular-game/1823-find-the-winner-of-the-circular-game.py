class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n+1)]
        index = 0
        while len(players) > 1:
            iterationCounter = 1
            while iterationCounter < k and len(players) > 1:
                index += 1
                iterationCounter += 1
            players.pop(index % len(players))
            index = index % (len(players) + 1)
        return int(players[0])


