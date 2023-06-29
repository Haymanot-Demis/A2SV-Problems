class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        isVertical = True
        for i in range(len(coordinates) - 1):
            if coordinates[i][0] != coordinates[i + 1][0]:
                isVertical = False
                break
            
        if isVertical:
            return True
            
        nemo = (coordinates[1][1] - coordinates[0][1])
        denom = (coordinates[1][0] - coordinates[0][0])

        if denom == 0:
            return False
        m = nemo / denom

        for i in range(len(coordinates) - 1):
            nemo = (coordinates[i + 1][1] - coordinates[i][1])
            denom = (coordinates[i + 1][0] - coordinates[i][0])
            if denom == 0:
                return False
            slope =  nemo / denom
            if slope != m:
                return False
            
        return True