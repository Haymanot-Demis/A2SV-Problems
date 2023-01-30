def circleOfStudents(nums, length):
    clockwise = [i for i in range(1, length + 1)]
    counter = clockwise[::-1]
    one = nums.index(1)
    check1 = nums[one:] + nums[:one]
    n_idx = nums.index(length)
    check2 = nums[n_idx:] + nums[:n_idx]
    if check1 == clockwise or check2 == counter:
        print("YES")
    else:
        print("NO")


testcases = int(input())
arrays = []
for _ in range(testcases):
    length = int(input())
    arrays.append([length, list(map(int, input().split()))])

for length, array in arrays:
    circleOfStudents(array, length)
