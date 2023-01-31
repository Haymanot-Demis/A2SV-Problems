class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        maxNum = int(sqrt(c))
        for i in range(maxNum + 1):
            if i*i + maxNum*maxNum == c:
                return True
            elif i*i + maxNum*maxNum > c:
                maxNum -= 1

        return False