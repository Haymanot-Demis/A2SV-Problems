class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        indx = 0
        length = len(arr)
        while indx < length - 1 and arr[indx] < arr[indx + 1]:
            indx += 1
        if indx == 0 or indx == length - 1:
            return False

        while indx < length - 1 and arr[indx] > arr[indx + 1]:
            indx += 1

        if indx < length - 1:
            return False
        return True