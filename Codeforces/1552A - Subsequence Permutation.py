def SubsequencePermutation(word:list):
    sorted_word = sorted(word)
    counter = 0
    for i in range(len(word)):
        if word[i] != sorted_word[i]:
            counter += 1
    print(counter)
                
testcases = int(input())
strings = []
for _ in range(testcases):
    length = (input("Enter length of string: "))
    strings.append(list(input("enter " + length + " length string: ")[:int(length)]))
for String in strings:
    SubsequencePermutation(String)