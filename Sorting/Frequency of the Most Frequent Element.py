# time = 30
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        maxFreq = 0;
        nums.sort()
        for i in range(1, len(nums)):
            maxOps = k
            freq = 1
            j = i - 1
            while j >= 0 and k > 0:
                diff = nums[i] - nums[j]
                maxOps -= diff
                if maxOps > 0:
                    #i.e have remaining operations
                    freq += 1
                elif maxOps == 0:
                    #i.e no more remaining operations
                    freq += 1
                    break
                else:
                    #i.e we can't make this with k operations
                    break
                j -= 1
            print("max frequency of", nums[i], freq)
            if maxFreq < freq:
                maxFreq = freq
        return maxFreq
