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
        # we can also use this to invert
        # x = list(x)
        # for i in range(len(x)):
        #     if x[i] == '0':
        #         x[i] = '1'
        #     else:
        #         x[i] = '0'
        # return ''.join(char for char in x)
        

    def reverse(self, x:str):
        return x[::-1]
        # we can also use these to reverse string
        # if x == '':
        #     return ''
        # return self.reverse(x[1:]) + x[0]

        # x = list(x)
        # i = 0
        # j = len(x) - 1
        # while i <= j - i:
        #     x[i], x[j - i] = x [j - i], x[i]
        #     i += 1
        # result = ''.join(char for char in x)
        # print(result)
        # return result

# ySolution = Solution()
# print(ySolution.findNthBinary(20))

