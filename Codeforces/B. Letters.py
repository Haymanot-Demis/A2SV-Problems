testcases = int(input())
for _ in range(testcases):
    length = int(input())
    message = sorted(input())[:length]
    print(ord(message[-1]) - ord('a') + 1)

