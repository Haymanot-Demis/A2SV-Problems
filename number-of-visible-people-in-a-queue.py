class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        length = len(heights)
        answer = [0] * length
        stack = []

        for right in range(length):
            while stack and heights[stack[-1]] < heights[right]:
                answer[stack.pop()] += 1
            if stack:
                answer[stack[-1]] += 1
            stack.append(right)
        
        return answer