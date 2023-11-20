class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch  == "]":
                encoded_string = []
                while stack and stack[-1] != "[":
                    encoded_string.append(stack.pop())

                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k += stack.pop()
                k = int(k[::-1])
                stack.append("".join(encoded_string[::-1] * k))
            else:
                stack.append(ch)

        return "".join(stack)