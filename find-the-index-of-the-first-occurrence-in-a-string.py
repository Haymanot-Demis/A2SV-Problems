class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0

        for i in range(len(needle), len(haystack)):
            if needle == haystack[left:i]:
                return left
            left += 1
        
        if needle == haystack[left:]:
            return left
        
        return -1