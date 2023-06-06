class Solution:
    def numDecodings(self, s: str) -> int:
        ways_to_decode = [0] * (len(s) + 1)
        ways_to_decode[-1] = 1
        if s[-1] != "0":
            ways_to_decode[-2] = 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] != "0" and 1 <= int(s[i:i+2]) <= 26:
                ways_to_decode[i] = ways_to_decode[i + 1] + ways_to_decode[i + 2]
            elif s[i] == "0":
                ways_to_decode[i] = 0
            else:
                ways_to_decode[i] = ways_to_decode[i + 1]

        return ways_to_decode[0]