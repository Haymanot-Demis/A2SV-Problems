class Solution:
    def trap(self, height: List[int]) -> int:
        right_greater = [0] * len(height)
        left_greater = [height[0]]
        right_greater[-1] = height[-1]

        for curr in range(1, len(height)):
            left_greater.append(max(height[curr], left_greater[curr - 1]))

        for curr in range(len(height) - 2, -1, -1):
            right_greater[curr] = (max(height[curr], right_greater[curr + 1]))
            
        return sum([ min(left_greater[i], right_greater[i]) - height[i] for i in range(len(height)) ])