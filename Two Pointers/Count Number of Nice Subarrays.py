class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        length = len(nums)
        niceSubarrays = 0
        counter = 0
        left = 0 
        right = 0
        while right < length:
            while right < length and counter != k:
                if nums[right] % 2 == 1:
                    counter += 1
                right += 1
            if counter != k and right == length:
                return niceSubarrays
            l = r = 1
            while nums[left] % 2 == 0:
                left += 1
                l += 1
            left += 1
            counter -= 1 
            while right < length and nums[right] % 2 == 0:
                right += 1
                r += 1
            niceSubarrays += r*l

        return niceSubarrays