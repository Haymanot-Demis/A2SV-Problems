import functools
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def mycomp(a, b):
            spaceindxA = a.index(" ")
            spaceindxB = b.index(" ")
            if a[spaceindxA + 1:] > b[spaceindxB + 1:]:
                return 1
            elif a[spaceindxA + 1:] < b[spaceindxB + 1:]:
                return -1
            elif a[spaceindxA + 1:] == b[spaceindxB + 1:]:
                if a[:spaceindxA] > b[:spaceindxB]:
                    return 1
                else:
                    return -1
            
        length = len(logs)
        right = length - 1
        digitLogCount = 0
        for left in range(length - 1, -1, -1):
            if logs[left].split()[1].isdigit():
                logs[left], logs[right] = logs[right], logs[left]
                right -= 1
                digitLogCount += 1
        logs[:length - digitLogCount] = sorted(logs[:length - digitLogCount], key = functools.cmp_to_key(mycomp))
        return logs
        