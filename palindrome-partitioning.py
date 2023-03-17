class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def backtrack(s, partition, ans):
            if not s:
                ans.append(partition)
                return 
            substr = ""
            for i, char in enumerate(s):
                substr += char
                if substr == substr[::-1]:
                    backtrack(s[i+1:], partition + [substr], ans)
        backtrack(s, [], ans)
        return ans