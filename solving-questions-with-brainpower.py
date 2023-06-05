class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        points = [0] * len(questions)
        points[-1] = questions[-1][0]
        for i in range(len(questions) - 2, -1, -1):
            points[i] = questions[i][0]
            
            if i + questions[i][1] + 1 < len(questions):
                points[i] += points[i + questions[i][1] + 1]

            points[i] = max(points[i], points[i + 1])
        
        return max(points)