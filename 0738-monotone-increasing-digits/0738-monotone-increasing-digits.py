class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        stack = list(map(int, list(str(n))))
        length = len(stack)
        i = 0
        while i < length - 1 and stack[i] <= stack[i + 1]:
            i += 1
        if i == length - 1:
            return n
        num = stack[i] - 1
        i -= 1
        while i >= 0 and num < stack[i]:
            num = stack[i] - 1
            i -= 1
        stack[i + 1] = num
        stack[i+2:] = [9]*(length - (i + 2 ))
        stack = map(str, stack)
        n = "".join(stack)
        return int(n)

