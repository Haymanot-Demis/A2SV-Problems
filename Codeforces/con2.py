def woringButton(string):
    buttons = set()
    i = 0
    length = len(string)
    if length == 1:
        print(string)
        return
    while i < length - 1:
        if string[i] == string[i + 1]:
            i += 2
        else:
            buttons.add(string[i])
            i += 1
    if i == length - 1:
        buttons.add(string[i])
    buttons = list(buttons)
    buttons.sort()
    print("".join(buttons))
 
testcases = int(input())
strings = []
for _ in range(testcases):
    strings.append(input())
for string in strings:
    woringButton(string)