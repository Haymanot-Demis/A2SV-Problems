def decodeToOriginalString(word):
    decoded_word = word[0]
    for i in range(1, len(word), 2):
        decoded_word += word[i]
    print(decoded_word)


testcases = int(input())
decoded_words = []
for _ in range(testcases):
    decoded_words.append(input())

for word in decoded_words:
    decodeToOriginalString(word)
