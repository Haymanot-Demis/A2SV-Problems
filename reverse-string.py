class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    def recursiveReverseString(self, s: List[str]) -> None:
        if not s:
            return []
        s = self.recursiveReverseString(s[1:]) + [s[0]]
        return s