class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        x_itr = 0
        y_itr = 0
        visited = set()
        matrix = [ [0 for  _ in range(n)] for _ in range(n)]
        i = 1
        for _ in range((n+1) // 2):
            while (x_itr, y_itr) not in visited and y_itr < n:
                matrix[x_itr][y_itr] = i
                visited.add((x_itr, y_itr))
                y_itr += 1
                i += 1
            x_itr += 1
            y_itr -= 1

            while (x_itr, y_itr) not in visited and x_itr < n:
                matrix[x_itr][y_itr] = i
                visited.add((x_itr, y_itr))
                x_itr += 1
                i += 1
            x_itr -= 1
            y_itr -= 1

            while (x_itr, y_itr) not in visited and y_itr >= 0:
                matrix[x_itr][y_itr] = i
                visited.add((x_itr, y_itr))
                y_itr -= 1
                i += 1
            x_itr -= 1
            y_itr += 1

            while (x_itr, y_itr) not in visited and x_itr >= 0:
                matrix[x_itr][y_itr] = i
                visited.add((x_itr, y_itr))
                x_itr -= 1
                i += 1
            x_itr += 1
            y_itr += 1

        return matrix