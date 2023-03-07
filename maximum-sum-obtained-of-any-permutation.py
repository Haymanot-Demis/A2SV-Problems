class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length = len(nums)
        max_sum = 0
        indices_count = [0] * length

        for start, end in requests:
            indices_count[start] += 1
            if end + 1 < length:
                indices_count[end + 1] -= 1
        for i in range(1, length):
            indices_count[i] += indices_count[i - 1]

        indices_count.sort(reverse=True)
        nums.sort(reverse=True)

        for indx in range(length):
            if indices_count[indx] == 0:
                return max_sum % (10**9 + 7)
            else:
                max_sum += indices_count[indx]*nums[indx]
        return max_sum % (10**9 + 7)