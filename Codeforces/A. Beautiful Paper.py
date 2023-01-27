def BeautifulPaper(rect1, rect2):
    if rect1[0] > 0 and rect2[0] > 0 and rect1[1] > 0 and rect2[1] > 0:
        max1 = max(rect1)
        min1 = min(rect1)
        max2 = max(rect2)
        min2 = min(rect2)
        if max1 == max2:
            if min1 + min2 == max1:
                print('YES')
            else:
                print('NO')
        else:
            print("NO")
    else:
        print("NO")


testcases = int(input())
rectangles = []
for _ in range(testcases):
    rect1 = list(map(int, input().split()))
    rect2 = list(map(int, input().split()))
    rectangles.append([rect1, rect2])
for rectangle in rectangles:
    BeautifulPaper(rectangle[0], rectangle[1])
