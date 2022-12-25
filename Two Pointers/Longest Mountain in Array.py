class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        peek = 1
        left = peek - 1
        right = peek + 1
        length = len(arr)
        mountainLength = 0
        for i in range(1, length - 1):
            left = i - 1
            right = i + 1
            while left >= 0 and arr[left] < arr[left + 1]:
                left -= 1
            print("left downhill", i - (left + 1))
            if left == i - 1:
                continue
            while right < length and arr[right] < arr[right - 1]:
                right += 1
            print("right downhill", (right - 1) - i)
            if right != i + 1:
                if mountainLength < right - (left + 1):
                    mountainLength = right - (left + 1)
            print("length ", mountainLength)
            if right >= length:
                break
        return mountainLength

