class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def validateOctet(octet):
            if not octet.isdigit():
                return False

            return (octet[0] != "0" if len(octet) > 1 else True) and int(octet) <= 255


        def validateHex(hex):
            for ch in hex:
                if not (ch.isdigit() or 97 <= ord(ch) <= 102 or 65 <= ord(ch) <= 70):
                    return False
            
            return 1 <= len(hex) <= 4

        x = queryIP.split(".") 
        isIPV4 = len(x) == 4
        for octet in x:
            val = validateOctet(octet)
            isIPV4 &= val
        
        if isIPV4:
            return "IPv4"

        x = queryIP.split(":") 
        isIPV6 = len(x) == 8

        for hex in x:
            val = validateHex(hex)
            isIPV6 &= val
        
        if isIPV6:
            return "IPv6"
        
        return "Neither"