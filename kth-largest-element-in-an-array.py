class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x : -x, nums))
        heapify(nums)
        
        for _ in range(k):
            ans = heappop(nums)
        
        return -ans