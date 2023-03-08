def createGroupsOfFour(programmers, mathematicians):
    return min(sum([programmers, mathematicians]) // 4, min(programmers, mathematicians))
testcases = int(input())
for _ in range(testcases):
    a, b = map(int, input().split())
    print(createGroupsOfFour(a, b))