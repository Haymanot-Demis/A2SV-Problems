from collections import Counter
def isFemale(username):
    distinicts = Counter(username)
    numOfDistinicts = len(distinicts)
    if numOfDistinicts % 2 == 1:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")
username = input()
isFemale(username)