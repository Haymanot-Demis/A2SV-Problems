class Solution():
    def Shell_Sort(self, nums:list):
        n = len(nums)
        gap = n//2

        while gap >= 1:
            j = gap
            while j < n:
                i =  j - gap
                val = nums[j]
                while i >= 0 and nums[i] > val:
                    nums[i + gap] = nums[i]
                    i -= gap
                nums[i + gap] = val
                j += 1
            gap //= 2

mySolution = Solution()
nums = [5, 8, 2, 4, 1, 3, 9, 7, 6, 0]
mySolution.Shell_Sort(nums)
print(nums)
