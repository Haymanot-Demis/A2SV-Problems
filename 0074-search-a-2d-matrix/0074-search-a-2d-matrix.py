class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        rowLength = len(matrix)
        colLength = len(matrix[0])
        rowToSearch = 0
        for row in range(rowLength):
            if target <= matrix[row][colLength - 1]:
                rowToSearch = row
                break
        
    
        isFound = target in matrix[rowToSearch]
        return isFound
        