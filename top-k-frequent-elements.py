# 10
class Solution(object):
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        sorted_nums = sorted(counter, key=lambda x : counter[x])
        
        return sorted_nums[-k:]