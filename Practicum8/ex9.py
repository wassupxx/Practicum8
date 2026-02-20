sentance = input()
words = ((sentance).lower()).split()
print(words)
for word in words:
    if words.count(word) == 2:
        print(word)
        break