class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #the number of iteration is row + 1 // 2
        row = len(matrix)
        col = len(matrix[0])
        answer = []
        x_itr = 0
        y_itr = 0
        visited = set()
        for _ in range((row + 1) // 2):
            while (x_itr, y_itr) not in visited and y_itr < col: # iterate to right
                answer.append(matrix[x_itr][y_itr])
                visited.add((x_itr, y_itr))
                y_itr += 1
            x_itr += 1
            y_itr -= 1
            while (x_itr, y_itr) not in visited and x_itr < row: # iterate to bottom
                answer.append(matrix[x_itr][y_itr])
                visited.add((x_itr, y_itr))
                x_itr += 1
            x_itr -= 1
            y_itr -= 1
            while (x_itr, y_itr) not in visited and y_itr >= 0: # iterate to left
                answer.append(matrix[x_itr][y_itr])
                visited.add((x_itr, y_itr))
                y_itr -= 1
            x_itr -= 1
            y_itr += 1
            while (x_itr, y_itr) not in visited and x_itr >= 0: # iterate to top
                answer.append(matrix[x_itr][y_itr])
                visited.add((x_itr, y_itr))
                x_itr -= 1
            x_itr += 1
            y_itr += 1
        return answer
        
