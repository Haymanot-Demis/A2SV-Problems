from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = SortedList()
        counts = [0] * len(nums)
        indx = -1
        for num in nums[::-1]:
            smallers = sorted_nums.bisect_left(num)
            sorted_nums.add(num)
            counts[indx] = smallers
            indx -= 1

        return counts