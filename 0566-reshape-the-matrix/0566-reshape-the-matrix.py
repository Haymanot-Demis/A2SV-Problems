class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        oneD = []
        rowLen = len(mat)
        colLen = len(mat[0])
        if r == rowLen:
            return mat
        else:
            for i in range(rowLen):
                for j in range(colLen):
                    oneD.append(mat[i][j])
            newMat = []
            if rowLen*colLen / r == c:
                k = 0
                while k < rowLen*colLen:
                    newMat.append(oneD[k:k + c])
                    k += c
                return newMat
            else:
                return mat