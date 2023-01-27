length = int(input())
encoded_string = list(map(str, input().split("0")))
number = ""
for ones in encoded_string:
    number += str(len(ones))
print(number)
