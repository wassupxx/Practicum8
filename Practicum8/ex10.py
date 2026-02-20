sentance = input()
words = sentance.split()
first_word = words[0]
result = []
for word in words[1:]:
    cleaned_word = ''.join(char for char in word if char.isalpha())
    if cleaned_word != first_word and len(set((cleaned_word).lower())) == len(cleaned_word):
        result.append(word)
print(result)


