text = input()
symbols = list(text.lower())
result = []
for symbol in symbols:
    if symbols.count(symbol) == 3:
        result.append(symbol)

if len(set(result)) == 1:
    print(result[0])
else:
    print("Не выполнено условие задания!")