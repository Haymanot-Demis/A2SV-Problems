class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0
        length = len(tickets)
        for indx in range(length):
            if indx > k:
                time_taken += min(tickets[indx], tickets[k] - 1)
            else:
                time_taken += min(tickets[indx], tickets[k])
        return time_taken