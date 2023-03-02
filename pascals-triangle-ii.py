class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        prev = self.getRow(rowIndex - 1)
        curr = [1]
        for indx in range(rowIndex - 1):
            curr.append(prev[indx] + prev[indx + 1])
        curr.append(1)
        return curr