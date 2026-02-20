def check_brackets(text):
    brackets = []
    for char in text:
        if char == '(':
            brackets.append(char)
        elif char == ')':
            if not brackets:
                return False
            brackets.pop()
    return len(brackets) == 0

print(check_brackets())