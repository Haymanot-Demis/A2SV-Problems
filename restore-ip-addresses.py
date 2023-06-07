class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        IPs = []

        def backtrack(indx, ip):
            if indx >= len(s):
                if len(ip) == 4:
                    IPs.append(".".join([str(decimal) for decimal in ip]))
                return 

            if s[indx] == "0":
                backtrack(indx + 1, ip + [0])
                return

            number = 0
            for j in range(indx, len(s)):
                number = number * 10 + int(s[j])
              
                if number > 255:
                    return 

                backtrack(j + 1, ip + [number])

        backtrack(0, [])
        return IPs