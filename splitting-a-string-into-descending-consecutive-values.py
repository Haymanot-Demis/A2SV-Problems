class Solution:
    def splitString(self, s: str) -> bool:
        ans = []
        def backtrack(indx):
            if indx >= len(s):
                return len(ans) >= 2
            
            for i in range(indx, len(s)):
                curr = int(s[indx:i + 1])
                if not ans or ans[-1] - 1 == curr:
                    ans.append(curr)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif curr - ans[-1] > 2:
                    break
                    
            return False
        return backtrack(0)