length = int(input())
cards = list(map(int, input().split()))
wube = 0
henok = 0
flag  = True
left = 0
right = length - 1
while left <= right:
    if flag:
        if cards[left] > cards[right]:
            wube += cards[left]
            left += 1
        else:
            wube += cards[right]
            right -= 1
        flag = False
    else:
        if cards[left] > cards[right]:
            henok += cards[left]
            left += 1
        else:
            henok += cards[right]
            right -= 1
        flag = True

print(wube, henok)
