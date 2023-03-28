class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = defaultdict(int, Counter(nums))
        missed_nums = []
        for i in range(1, len(nums) + 1):
            if not count[i]:
                missed_nums.append(i)
        return missed_nums