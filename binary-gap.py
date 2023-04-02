class Solution:
    def binaryGap(self, n: int) -> int:
        prev_one_pos = -1
        curr_pos = 0
        binary_gap = 0
        while n:
            if n & 1 and prev_one_pos == -1:
                prev_one_pos = curr_pos
            elif n & 1:
                binary_gap = max(binary_gap, curr_pos - prev_one_pos)
                prev_one_pos = curr_pos
            curr_pos += 1
            n >>= 1
        return binary_gap