#time = 45
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        NthBinary = self.findNthBinary(n)
        return NthBinary[k - 1]

    def findNthBinary(self, n: int) -> str:
        if n <= 1:
            return "0"
        binary = self.findNthBinary(n - 1)
        invertedBinary = self.invert(binary)
        return binary + "1" + self.reverse(invertedBinary)
         

    def invert(self, x:str):
        x = x.replace("0","x")
        x = x.replace("1","0")
        x = x.replace("x","1")
        return x

    def reverse(self, x:str):
        return x[::-1]