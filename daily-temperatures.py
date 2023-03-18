class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            # the concept behind this solution is evry element in the is less than the preceding number(greater than its next element) because if not the number before it will be the warmer day for it but it is not that is why it it is after it 
            while stack and temperatures[stack[-1]] < temp:
                leftIndex = stack.pop()
                answer[leftIndex] = i - leftIndex
            stack.append(i)
        return answer