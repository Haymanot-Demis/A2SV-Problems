from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = SortedList([])
        counter = defaultdict(int)

        total_cost = 0

        for num in instructions:
            pos = nums.bisect_right(num)

            smallers = pos - counter[num]
            greaters = len(nums) - pos

            counter[num] += 1
            nums.add(num)

            cost = min(smallers, greaters)
            total_cost += cost

        return total_cost  % (10 ** 9 + 7)