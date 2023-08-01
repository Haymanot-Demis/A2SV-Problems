class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = defaultdict(int)

        def dp(indx1, indx2):
            if (indx1, indx2) in memo:
                return memo[(indx1, indx2)]
            
            if indx1 >= len(s1) or indx2 >= len(s2):
                return 0, ""
            ASCII_sum = 0
            subseq = ""
            if s1[indx1] == s2[indx2]:
                res = dp(indx1 + 1, indx2 + 1)
                ASCII_sum +=  res[0] + ord(s1[indx1])
                subseq += s1[indx1] + res[1]
            else:
                res1 = dp(indx1 + 1, indx2)                 
                res2 = dp(indx1, indx2 + 1)
                ASCII_sum, subseq = max(res1, res2)
            memo[(indx1, indx2)] = (ASCII_sum, subseq)
            return memo[(indx1, indx2)]

        ASCII_sum, subseq = dp(0, 0)
        counter = Counter(s1 + s2)
        total_ascii = 0
        for letter, freq in counter.items():
            total_ascii += ord(letter) * freq

        return total_ascii - 2 * ASCII_sum