testcases = int(input())
for _ in range(testcases):
    string = input()
    hashMap = {}
    hashMap[string[0]] = 0
    left = 0
    minLen = len(string)
    flag = False
    for i in range(1, len(string)):
        hashMap[string[i]] = i
        # if string[i] == string[min(hashMap.values())]:
        #     left = min(hashMap.values()) + 1
        #     hashMap[string[i]] = i
        #     # to remove duplicates from left
        #     while left < i and string[left] == string[left + 1]:
        #         left += 1
        if len(hashMap) == 3:
            flag = True
            minLen = min(minLen, i - min(hashMap.values()) + 1)

    if flag:
        print(minLen)
    else:
        print(0)
