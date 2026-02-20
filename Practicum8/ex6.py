sentance = input()
sentances = [word for word in sentance.split()]
reverse = sentances[::-1]
for word in reverse:
    print(word, end=' ')


