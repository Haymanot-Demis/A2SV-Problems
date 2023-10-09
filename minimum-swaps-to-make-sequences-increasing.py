class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        """
        with swapping the current numbers and with out see which will bring smaller number of swaps
        """            

        memo = {}

        def dp(prev1, prev2, indx, isSwapped):
            if indx == len(nums1):
                return 0
            if (indx, isSwapped) in memo:
                return memo[(indx, isSwapped)]
            
            swaps = 2 ** 31
            if nums1[indx] > prev1 and nums2[indx] > prev2:
                swaps = dp(nums1[indx], nums2[indx], indx + 1, 0)
            
            if nums1[indx] > prev2 and nums2[indx] > prev1:
                swaps = min(swaps, 1 + dp(nums2[indx], nums1[indx], indx + 1, 1))

            memo[(indx, isSwapped)] = swaps
            return swaps
        
        return dp(-1, -1, 0, 0)