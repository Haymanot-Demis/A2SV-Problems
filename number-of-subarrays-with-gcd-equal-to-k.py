class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            _gcd = nums[i]
            for j in range(i, len(nums)):
                _gcd = gcd(_gcd, nums[j])
                if _gcd == k:
                    ans += 1
                if _gcd < k:
                    break
        return ans