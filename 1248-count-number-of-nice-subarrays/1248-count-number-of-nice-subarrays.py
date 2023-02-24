class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        replace odds with 1 and evens with 0 the compute the prefix sum of that list, then if we have k number of odds now add the number of  => current count of odds minus k , from the dictionary that we saved each count successively
        or the core concept is we can know how many odds are there between any two indices after we built the prefix sum of the number odds
        """
        length = len(nums)
        niceSubarrays_count = 0
        dictionary = defaultdict(int)

        dictionary[0] = 1
        nums[0] = nums[0] % 2
        dictionary[nums[0] % 2] += 1
        niceSubarrays_count += dictionary[nums[0] - k]

        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i] % 2
            niceSubarrays_count += dictionary[nums[i] - k]
            dictionary[nums[i]] += 1

            
        return niceSubarrays_count