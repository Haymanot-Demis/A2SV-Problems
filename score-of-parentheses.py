class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        total_score = 0
        for char in s:
            if char == "(":
               stack.append(char)
            else:
                score = 0
                while stack[-1] != "(":
                    score += stack.pop()
                stack.pop()
                if score:
                    stack.append(score*2) 
                else:
                    stack.append(1)  
      
        return sum(stack)