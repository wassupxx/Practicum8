text = input()
symbols = list(text)
consistent_symbols = 1
count_symbols = 1
previous_symbol = symbols[0]
for symbol in symbols[1:]:
    if symbol == previous_symbol:
        count_symbols += 1
    else:
        consistent_symbols = max(consistent_symbols, count_symbols)
        count_symbols = 1
        previous_symbol = symbol
consistent_symbols = max(consistent_symbols, count_symbols)
print(consistent_symbols)