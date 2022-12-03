class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = list()
        for char in s:
            if (ord(char) <= 122 and ord(char) >= 97) or char == '(':
                stack.append(char)
            elif char == ')':
                substing = ''
                while stack[-1] != '(':
                    substing += stack.pop()
                stack.pop()
                for subchar in substing:
                    stack.append(subchar)
        reversedString = ''  
        for char in stack:
            reversedString += char
        return reversedString