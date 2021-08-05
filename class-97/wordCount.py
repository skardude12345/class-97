text = input('write something: ')

wordCount = 1
characterCount = 0
for word in text:
    if word==' ':
        wordCount += 1

    if word!=' ':
        characterCount += 1

print('Number of Words: ', wordCount)
print('Number of Letters: ', characterCount)


    