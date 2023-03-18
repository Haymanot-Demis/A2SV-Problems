class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        the key of this problem is the first and last half of the string is inverted form of one an other
        """
        if n == 1:
            return 0
        if n == 2:
            return int("01"[k - 1])
 
        if k > 2 ** (n - 2):
            prevK = self.kthGrammar(n - 1, k - 2 ** (n - 2))
            return int(not(prevK))
        prevK = self.kthGrammar(n - 1, k) 
        return prevK