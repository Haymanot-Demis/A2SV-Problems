class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = Counter(s)
        visited = set()
        stack = []
        for char in s:
            if char not in visited:
                while stack and char < stack[-1] and counter[stack[-1]]:
                    visited.remove(stack.pop())
                stack.append(char)
                visited.add(char)
                counter[char] -= 1
            else:
                counter[char] -= 1
        return "".join(stack)