class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ends_with = defaultdict(int)
        
        for i in range(len(arr)):
            if ends_with[arr[i] - difference] :
                ends_with[arr[i]] = ends_with[arr[i] - difference] + 1
            else:
                ends_with[arr[i]] = 1
                        
        return max(ends_with.values())