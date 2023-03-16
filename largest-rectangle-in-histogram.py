class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        finding the maximum possible area that canbe made with the height of each bar
        """
        stack = []
        max_area = 0
        length = len(heights)
        prev_smaller = [-1] * length
        next_smaller = [length] * length

        for i in range(length):
            while stack and heights[stack[-1]] > heights[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)

        stack = []

        for indx in range(length):

            while stack and heights[stack[-1]] >= heights[indx]:
                stack.pop()
            if stack and heights[stack[-1]] < heights[indx]:
                prev_smaller[indx] = stack[-1]

            stack.append(indx)

            w = next_smaller[indx] - prev_smaller[indx] - 1
            max_area = max(max_area, w * heights[indx])
                    
        
        return max_area