class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def find(sub, full):
            if sub == "":
                return True
            pos = full.find(sub[0])
            if pos == -1:
                return False
            return find(sub[1:], full[pos+1:])
        return find(s, t)