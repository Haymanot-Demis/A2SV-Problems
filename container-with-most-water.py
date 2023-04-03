class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        using two pointers to take the window that can give us maximum area. Its working priciple is is to get the max area/water container
        take two end pointes then narrwo the window from the smaller side if we can get a better height than its current height so that we can have better and always take the maximum area from the current and previous  
        """
        length = len(height)
        left = 0
        right = length - 1
        maxArea = 0
        while left < right:
            width = right - left
            maxArea = max(maxArea, min(height[left], height[right]) * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea