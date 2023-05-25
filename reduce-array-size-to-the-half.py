class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = list(Counter(arr).values())
        counter.sort(reverse=True)
        removed = 0
        i = 0
        while removed < len(arr) // 2:
            removed += counter[i]
            i += 1
        
        return i