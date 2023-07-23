class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        memo = defaultdict(lambda : 0, { (0,1) : 1 })

        for i in range(1, len(nums)):
            temp_memo = defaultdict(lambda : 0, {(i, 1):1})
            max_len = 1
            for key, count in memo.items():
                indx, _len = key
                if nums[i] > nums[indx]:
                    max_len = max(_len + 1, max_len)
                    temp_memo[(i, _len + 1)] = temp_memo[(i, _len + 1)] + max(count, 1)
            memo[(i, max_len)] = temp_memo[(i, max_len)]
        
        max_len = 0
        max_count = 0
        for key, count in memo.items():
            indx, _len= key
            if _len > max_len:
                max_len = _len
                max_count = count
            elif _len == max_len:
                max_count += count

        return max_count