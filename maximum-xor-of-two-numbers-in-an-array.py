class Trie:
    def __init__(self, max_bit_len):
        self.root = {}
        self.max_bit_len = max_bit_len 

    def insert(self, num) -> None:
        node = self.root

        for p in range(self.max_bit_len, -1, -1):
            bit = (num >> p) & 1
            if bit not in node:
                node[bit] = {}
            
            node = node[bit]
    
    def getMaxXOR(self, num):
        node = self.root
        xor = 0

        for p in range(self.max_bit_len, -1, -1):
            bit = (num >> p) & 1

            if (1 - bit) in node:
                xor += 2 ** p
                node = node[1 - bit]
            else:
                node = node[bit]    

        return xor

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_bit_len = int.bit_length(max(nums))
        trie = Trie(max_bit_len)
        root = {}

        for num in nums:
            trie.insert(num)

        ans = 0
        for num in nums:
            ans = max(ans, trie.getMaxXOR(num))
        
        return ans