class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        numOfCoins = 0
        length = len(piles)
        indexToStop = length//3 - 1
        for i in range(length - 2, indexToStop , -2):
            # the core idea of this solution is that the coin that I am gonna take is always 
            # the 2nd largest number from the two numbers taken from end of the array
            # it will done  length//3 times
            numOfCoins += piles[i]
        return numOfCoins