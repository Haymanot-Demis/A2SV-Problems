class Solution:
    def calculate(self, s: str) -> int:
        # given string as prefix we have to change to post fix using stack
        s = s.replace(" ", "")
        infix = []
        left = 0
        right = 1
        while right < len(s):
            if s[right] == "/" or s[right] == "*" or s[right] == "+" or s[right] == "-":
                infix.append(s[left:right])
                infix.append(s[right])
                left = right + 1
            right += 1
        infix.append(s[left:])
        print(infix)
        stack = []
        operator = "+"
        for char in infix:
            if char.isdigit():
                if operator == "+":
                    stack.append(int(char))
                elif operator == "-":
                    stack.append(-int(char))
                elif operator == "*":
                    stack.append(stack.pop() * int(char))
                elif operator == "/":
                    stack.append(int(stack.pop() / int(char)))
            else:
                operator = char
        for i in range(1, len(stack)):
            stack[i] += stack[i - 1]
        return int(stack[-1])