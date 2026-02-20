import string

sentance = input()
translator = str.maketrans('', '', string.punctuation)
cleaned = sentance.translate(translator)
words = cleaned.split()
min_length = len(words[0])
for word in words:
    if len(word) < min_length:
        min_length = len(word)
print(min_length)
