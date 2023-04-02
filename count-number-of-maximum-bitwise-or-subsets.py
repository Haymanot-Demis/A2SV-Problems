class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        length = len(nums)
        n = 2 ** length
        subsets_OR = []
        max_subset_OR = 0
        for i in range(n):
            subset = []
            OR = 0
            for j in range(length):
                if i & 1 << j:
                    OR |= nums[j]
            max_subset_OR = max(max_subset_OR, OR)
            subsets_OR.append(OR)

        answer = 0
        for subset_OR in subsets_OR:
            if max_subset_OR == subset_OR:
                answer += 1
        return answer