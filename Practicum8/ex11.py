game = input()
cities = (game.lower()).split()
error_found = False
for index in range(len(cities) - 1):
    if ((cities[index])[-1]) != ((cities[index + 1])[0]):
        error_found = True
        mistake = index + 1
        break
if not error_found:
    if len(cities) % 2 == 1:
        result = "Победитель - Петя!"
    else:
        result = "Победитель - Вася!"
else:
    if mistake % 2 == 0:
        result = "Победитель - Петя!"
    else:
        result = "Победитель - Вася!"
print(result)
