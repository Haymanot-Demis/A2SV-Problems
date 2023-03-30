class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = 0
            j = i
            while j != 0:
                if j & 1:
                    count += 1
                j = j >> 1
            ans.append(count)
        return ans