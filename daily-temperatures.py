class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                leftIndex = stack.pop()
                answer[leftIndex] = i - leftIndex
            stack.append(i)
        return answer

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]: # has hign running time
        answer = list()
        for i in range(len(temperatures)):
            count = 0
            for j in range(i + 1, len(temperatures)):
                if (temperatures[j] > temperatures[i]):
                    count = j - i
                    break
                
            answer.append(count)
        return answer