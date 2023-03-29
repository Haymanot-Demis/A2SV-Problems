class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        strs = zip(*strs)
        for column in strs:
            if (list(column) != sorted(column)):
                count += 1
        return count