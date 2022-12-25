class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))

        for i in range(k-1):
            right = len(nums)
            left = right - 2
            while left >= 0:
                large = max(nums[left:right])
                if  large != nums[left]:
                    num = large
                    indx = 0
                    i = left + 1
                    while i < right:
                        if nums[i] > nums[left] and nums[i] < num:
                            num = nums[i]
                            indx = i
                        i += 1
                    if num == large:
                        indx = nums[left:right].index(large) + left
                    nums[left], nums[indx] = nums[indx], nums[left]
                    temp = sorted(nums[left + 1:right])
                    nums[left + 1:right] = temp
                    break
                left -= 1
            if left == -1:
                nums.sort()
        return "".join(str(num) for num in nums)