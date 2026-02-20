first_raw = input()
second_raw = input()
third_raw = input()
first = list(first_raw.lower())
second = list(second_raw.lower())
third = list(third_raw.lower())
result = []
for symbol in first:
    if (symbol in second) == False and (symbol in third)==False:
        result.append(symbol)
for symbol in second:
    if (symbol in first) == False and (symbol in third)==False:
        result.append(symbol)
for symbol in third:
    if (symbol in first) == False and (symbol in second)==False:
        result.append(symbol)
print(result)
