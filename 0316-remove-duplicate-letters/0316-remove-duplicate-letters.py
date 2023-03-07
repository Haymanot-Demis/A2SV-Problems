class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = set()
        last_occurence_index = {char:indx for indx, char in enumerate(s)}
        stack = []
        for curr_index in range(len(s)):
            if s[curr_index] not  in visited:
                while stack and stack[-1] >= s[curr_index] and last_occurence_index[stack[-1]] > curr_index:
                    visited.remove(stack.pop())
                stack.append(s[curr_index])
                visited.add(s[curr_index])
        return "".join(stack)
        