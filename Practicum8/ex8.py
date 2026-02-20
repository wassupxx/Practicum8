import string

sentance = input()
translator = str.maketrans('', '', string.punctuation)
clean_sentance = sentance.translate(translator)
words = clean_sentance.split()
sorted_words = sorted(words, key = len)
print(sorted_words)