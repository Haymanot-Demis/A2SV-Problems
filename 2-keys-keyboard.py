class Solution:
    def minSteps(self, n: int) -> int:
        def steps(x):
            if x == 1:
                return 0

            for i in range(x // 2, 0, -1):
                if x % i == 0:
                    return steps(i) + x // i
        return steps(n)