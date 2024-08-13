class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = []
        
        counter = Counter(nums)
        
        for num, freq in counter.items():
            heappush(top_k, (freq, num))
            
            if len(top_k) > k:
                heappop(top_k)
        
        ans = []
        for freq, num in top_k:
            ans.append(num)
        
        return ans
            