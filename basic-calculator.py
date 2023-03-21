class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        index = 0
        length = len(s)
        def getInterger(index, length, s):
            number = ""
            while index < length and s[index].isnumeric():
                number += s[index]
                index += 1
            return number, index - 1

        while index < length:
            char = s[index]
            if char == " " or char == "+":
                index += 1
                continue 
            if not stack or char in "(-":
                if char.isnumeric():
                    number, index = getInterger(index, length, s)
                    stack.append(int(number))
                else:    
                    stack.append(char)
            elif char.isnumeric():
                number, index = getInterger(index, length, s)
                if stack[-1] == "-":
                    stack[-1] = -int(number)
                else:
                    stack.append(int(number))
            else:
                result = 0
                while stack and stack[-1] != "(":
                    result += stack.pop()
                stack.pop()
                if stack and stack[-1] == "-":
                    result = -result
                    stack.pop()
                stack.append(result)
            index += 1
        return sum(stack)


        return 0