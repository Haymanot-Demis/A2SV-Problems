class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            stack.append(ast)
            while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
                x = stack.pop()
                y = stack.pop()

                if abs(x) > abs(y):
                    stack.append(x)
                elif abs(y) > abs(x):
                    stack.append(y)

        return stack