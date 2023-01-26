length, k = list(map(int, input().split()))
num = list(map(int, input().split()))
num.sort()
if k == 0:
    if num[0] - 1 >= 1 and num[0] - 1 < num[0]:
        print(num[0] - 1)
    else:
        print("-1")
elif k < length and num[k - 1] == num[k]:
    print(-1)
else:
    print(num[k - 1])