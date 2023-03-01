class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0
        length = len(tickets)
        indx = 0
        while tickets[k] != 0:
            if tickets[indx % length] != 0:
                time_taken += 1
                tickets[indx % length] -= 1
            indx += 1
        return time_taken