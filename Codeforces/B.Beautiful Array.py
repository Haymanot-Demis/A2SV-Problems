def Print(Set):
    print(len(Set), end=" ")
    for num in Set:
        print(num, end=" ")
    print()

length = int(input())
nums = list(map(int, input().split()))
negatives = set()
positives = set()
zeroes = set()
set1 = set()
set2 = set()
set3 = set()

for i in range(length):
    if nums[i] < 0:
        negatives.add(i)
    elif nums[i] > 0:
        positives.add(i)
    else:
        zeroes.add(i)

if positives: 
    for i in positives:
        set2.add(nums[i])
    set1.add(nums[negatives.pop()])
    for i in negatives:
        set3.add(nums[i])
    for i in zeroes:
        set3.add(nums[i])
else:
    for i in range(2):
        set2.add(nums[negatives.pop()])
    set1.add(nums[negatives.pop()])
    for i in negatives:
        set3.add(nums[i])
    for i in zeroes:
        set3.add(nums[i])

Print(set1)
Print(set2)
Print(set3)



