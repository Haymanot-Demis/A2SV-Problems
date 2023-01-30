def ColoringNumber(numbers: list, length):
    numbers.sort()
    left = 0
    right = length - 1
    red = [0, []]
    blue = [0, []]
    while left < right:
        red[1].append(numbers[right])
        red[0] += numbers[right]
        right -= 1
        while left <= right and blue[0] + numbers[left] < red[0]:
            blue[1].append(numbers[left])
            blue[0] += numbers[left]
            left += 1

        if red[0] > blue[0] and len(blue[1]) > len(red[1]):
            print("YES")
            return

    if red[0] > blue[0] and len(blue[1]) > len(red[1]):
        print("YES")
    else:
        print("NO")


testcases = int(input())
numbers = []
for _ in range(testcases):
    length = int(input())
    numbers.append([length, list(map(int, input().split()))])

for length, number in numbers:
    ColoringNumber(number, length)
