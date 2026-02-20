text = input("Enter a sentence: ")
symbols = list(text)
consistent_space = 0
space = 0
print(symbols)
for symbol in symbols:
    if symbol.isspace():
        space += 1
    else:
        consistent_space = max(consistent_space, space)
        space = 0
print(max(space, consistent_space))
