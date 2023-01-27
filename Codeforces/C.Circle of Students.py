def circleOfStudents(arr):
    length = len(arr) - 1
    for i in range(length - 1):
        if abs(arr[i] - arr[i + 1]) != 1 and max(arr[i], arr[i + 1]) != length and min(arr[i], arr[i + 1]) != 1:
            print("NO")
            return
    print("YES")


testcases = int(input())

arrStudents = []
for _ in range(testcases):
    length = int(input())
    arrStudents.append(list(map(int, input().split())))
for students in arrStudents:
    circleOfStudents(students)
