class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        return int((-1 + math.sqrt(1 + 8 * len(grades))) // 2)