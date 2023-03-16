class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total_water = 0
        for right in range(len(height)):
            while stack and height[stack[-1]] <= height[right]:
                middle = stack.pop()
                if stack:
                   h = min(height[stack[-1]], height[right]) - height[middle] 
                   w = right - stack[-1] - 1
                   total_water += h * w
            stack.append(right)
        return total_water