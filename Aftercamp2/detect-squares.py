class DetectSquares:

    def __init__(self):
        self.points = defaultdict(set)
        self.freq = defaultdict(int)        

    def add(self, point: List[int]) -> None:
        self.points[point[0]].add(tuple(point))
        self.freq[tuple(point)] += 1        

    def count(self, point: List[int]) -> int:
        x_axis = self.points[point[0]]
        squares = 0

        for p in x_axis:
            if p[1] != point[1]:

                # to left
                s = abs(point[1] - p[1])
                p1 = (p[0] - s, p[1])
                p2 = (p[0] - s, point[1])

                squares += self.freq[p1] * self.freq[p2] * self.freq[p]

                p1 = (p[0] + s, p[1])
                p2 = (point[0] + s, point[1])

                squares += self.freq[p1] * self.freq[p2] * self.freq[p]
        return squares

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)