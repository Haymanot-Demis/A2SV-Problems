class Solution:
    def numberOfOnes(self,n:list[int],l : int,r:int) -> int:
        self.convertToOnesAndZeros(n,0)
        count = 0
        for i in range(l-1,r):
            if n[i] == 1:
                count += 1
        return count

    def convertToOnesAndZeros(self,n, indx):
        print(n, indx)
        if indx == len(n):
            return n
        if n[indx] != 1 and n[indx] != 0:
                tempList = [int(n[indx]/2),int(n[indx] % 2), int(n[indx]/2)]
                n[indx:indx] = tempList
                n.pop(indx+3)
        if n[indx] != 1 and n[indx] != 0:
            return self.convertToOnesAndZeros(n, indx);
        return self.convertToOnesAndZeros(n, indx + 1);

mySolution = Solution()
print(mySolution.numberOfOnes([10],3,10))