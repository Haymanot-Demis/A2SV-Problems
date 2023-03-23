class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        monotonic_stack = []
        length = len(arr)
        # chunks = []
        chunk_count = 0
        left = 0
        for right in range(length):
            while monotonic_stack and monotonic_stack[-1] < arr[right]:
                monotonic_stack.pop()
            monotonic_stack.append(arr[right])
            if monotonic_stack and monotonic_stack[0] == right:
                # chunks.append(arr[left:right + 1])
                chunk_count += 1
                left = right + 1
        return chunk_count