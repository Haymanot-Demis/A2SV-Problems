class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dfs(image, set(), sr, sc, image[sr][sc] ,color)
        return image

    def dfs(self, image, visited, row, col, prev_color, new_color):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        inbound = 0 <= row < len(image) and 0 <= col < len(image[0])
        if not inbound or image[row][col] != prev_color or (row, col) in visited:
            return
        
        image[row][col] = new_color
        visited.add((row, col))

        for horiz, vertic in directions:
            self.dfs(image, visited, row + horiz, col + vertic, prev_color, new_color)