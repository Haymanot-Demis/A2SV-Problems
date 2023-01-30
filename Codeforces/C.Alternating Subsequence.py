def alternateSequence(sequence: list, length):
    alternate_sequence = [sequence[0]]
    flag = sequence[0] > 0
    for num in sequence:
        if (flag and num > 0) or (not flag and num < 0):
            alternate_sequence[-1] = max(alternate_sequence[-1], num)
        elif (not flag and num > 0) or (flag and num < 0):
            alternate_sequence.append(num)
            flag = num > 0
    print(sum(alternate_sequence))


testcases = int(input())
sequences = []
for _ in range(testcases):
    length = int(input())
    sequences.append([length, list(map(int, input().split()))])
for length, sequence in sequences:
    alternateSequence(sequence, length)
