class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """
        The idea of this solution is the batteries which are less than or equal to the minues that we assumed the computers can runs simultaneouly can be used fully, so we can add them all and we have this much battery that can be equally distributed accros the computers. Then if we have average batteries per computers more than or equal to the current minutes we could be able to run computer more than this time so move left up. 
        """
        low = 1
        high = sum(batteries) // n
        ans = 1

        while low <= high:
            mid = high - (high - low) // 2

            total = 0
            for i in range(len(batteries)):
                total += min(batteries[i], mid)
            
            if total // n >= mid:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans