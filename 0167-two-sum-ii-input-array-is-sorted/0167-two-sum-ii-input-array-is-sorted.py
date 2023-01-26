class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        left = 0
        right = length - 1
        while left < right:
            Sum = numbers[left] + numbers[right]
            if Sum == target:
                return[left + 1, right + 1]
            elif Sum > target:
                right -= 1
            else:
                left += 1
