from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        """
        first rearrange the formula like this  nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff
        this means finding differece of corresponding elements that is an other array and we are asked to find any pair from these differences so that corresponding_diff[i] <= corresponding_diff[j] + diff where i < j
        """

        diff_arr = [nums1[i] - nums2[i] for i in range(len(nums1))]
        sorted_arr = SortedList([diff_arr[0]])
        pairs_count = 0
        
        for i in range(1, len(nums1)):
            pairs_count += sorted_arr.bisect_right(diff_arr[i] + diff)
            sorted_arr.add(diff_arr[i])
        
        return pairs_count