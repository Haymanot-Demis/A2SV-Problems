class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        counter = defaultdict(int)

        total_cost = 0

        for num in instructions:
            pos = bisect_right(nums, num)

            smallers = pos - counter[num]
            greaters = len(nums) - pos

            counter[num] += 1
            nums.insert(pos, num)

            cost = min(smallers, greaters)
            total_cost += cost

        return total_cost  % (10 ** 9 + 7)