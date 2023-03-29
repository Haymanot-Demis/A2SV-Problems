class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        prev_max = -1
        for indx in range(length - 1, -1, -1):
            prev_max, arr[indx] = max(prev_max, arr[indx]), prev_max
        return arr