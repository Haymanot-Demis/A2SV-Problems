length, busCapacity = list(map(int, input().split()))
busQueue = list(map(int, input().split()))
busCounter = 0
pointer = 0
while pointer < length:
    currpassengers = 0
    while pointer < length and currpassengers < busCapacity:
        if busQueue[pointer] <= busCapacity - currpassengers:
            currpassengers += busQueue[pointer]
            pointer += 1
        elif busQueue[pointer] > busCapacity - currpassengers:
            break
    busCounter += 1
print(busCounter)
