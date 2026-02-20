math_expression = input()
tokens = list(math_expression.replace(' ', ''))
for token in tokens:
    if token == '(':
        print(tokens.index(token))
        tokens_reversed = list(reversed(tokens))
        for token in tokens_reversed:
            if token == ')':
                print(tokens_reversed.index(token))
print(tokens)