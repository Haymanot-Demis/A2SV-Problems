def K_Ladder(planks: list):
    planks.sort()
    length = len(planks)
    height = min(planks[-2:]) - 1
    print(min(height, length - 2))


testcases = int(input())
planks = []
for _ in range(testcases):
    length = input()
    planks.append(list(map(int, input().split())))
for palnk in planks:
    K_Ladder(palnk)
