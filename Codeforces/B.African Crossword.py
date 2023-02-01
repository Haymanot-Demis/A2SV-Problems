from collections import Counter
m, n = map(int, input().split())
crossword = []
for _ in range(m):
    crossword.append(input())

rowCount = []
for i in range(m):
    rowCount.append(Counter(crossword[i]))

colCount = list(zip(*crossword))
for i in range(n):
    colCount[i] = Counter(colCount[i])

word = ""
for row in range(m):
    for col in range(n):
        if rowCount[row][crossword[row][col]] == 1 and colCount[col][crossword[row][col]] == 1:
            word += crossword[row][col]
print(word)
