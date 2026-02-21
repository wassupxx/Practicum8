def transfers(text, width):
    words = text.split()
    strings = []
    current_string = []
    current_length = 0

    for word in words:

        if current_length + len(word) + (1 if current_string else 0) <= width:
            current_string.append(word)
            current_length += len(word) + (1 if current_string else 0)
        else:

            strings.append(' '.join(current_string))
            current_string = [word]
            current_length = len(word)

    strings.append(' '.join(current_string))

    result = []
    for string in strings:
        if len(string) < width:
            string += ' ' * (width - len(string))
        result.append(string)

    return '\n'.join(result)

text = input()
width = int(input())
print(transfers(text,width))
