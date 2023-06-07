class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            _lcm = nums[i]

            for j in range(i, len(nums)):
                _lcm = lcm(_lcm, nums[j])

                if _lcm == k:
                    ans += 1
                
                if _lcm > k:
                    break
        return ans