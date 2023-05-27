class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        right_min = -1
        pos_to_change = -1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[right_min]:
                pos_to_change = i
                break
            else:
                right_min = i

        if pos_to_change == -1:
            return arr

        pair = right_min
        for i in range(pos_to_change + 1, len(arr)):
            if arr[i] < arr[pos_to_change] and arr[i] > arr[pair]:
                pair = i
        arr[pair], arr[pos_to_change] = arr[pos_to_change], arr[pair]
        return arr