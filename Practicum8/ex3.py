sentance = input()
symbols = (list(sentance.lower()))
letters = []
for symbol in symbols:
    if symbol.isalpha():
        letters.append(symbol)
result=list(set(letters))
print(len(result))
