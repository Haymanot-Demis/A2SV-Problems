class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times     
        self.winners = [0] * (len(self.persons) + 1)
        hashtable = defaultdict(int)
        for indx, person in enumerate(self.persons):
            hashtable[person] += 1
            if hashtable[person] >= hashtable[self.winners[indx - 1]]:
                self.winners[indx] = person
            else:
                self.winners[indx] = self.winners[indx - 1]

    def q(self, t: int) -> int:
        

        pos = bisect_right(self.times, t) - 1
        return self.winners[pos]        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)