class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        round = 0
        for task, count in counter.items():
            if count % 3 == 0:
                round += count // 3
            elif count > 1:
                round += count // 3 + 1
            else:
                return -1
            
        return round