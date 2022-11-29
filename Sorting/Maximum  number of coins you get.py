#time 25
class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        print(piles)
        numOfCoins = 0
        for i in range(len(piles) - 2, len(piles)/3 - 1, -2):
            # the core idea of this solution is that the coin that I am gonna take is always 
            # the 2nd largest number from the two numbers taken from end of the array
            print(i, piles[i])
            numOfCoins += piles[i]
            print(numOfCoins)
        return numOfCoins