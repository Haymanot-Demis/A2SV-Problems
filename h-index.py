class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        countingPrefixSum = []
        hindex = 0
        length = len(citations) # the length is equal to the total number of citaions
        for value in range(min(length, max(citations)) + 1):
            left_pos = bisect_left(citations, value)
            right_pos = bisect_right(citations, value)
            for pos in range(left_pos, right_pos + 1):
                if length - pos == value:
                    hindex = value

        return hindex