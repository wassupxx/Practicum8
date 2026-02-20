number = int(input())
print("\n" * 25)
attempts = 10
while attempts > 0:
    trying = input()
    bulls = 0
    cows = 0
    for placement in range(len(str(number))):
        if int(trying[placement]) == int(str(number)[placement]):
            bulls += 1
        elif trying[placement] in str(number):
            cows += 1
    print(f"Быков:{bulls} Коров:{cows}")
    if bulls == (len(str(number))) and cows == 0:
        print("Победа!")
        break
    attempts -= 1
    if attempts == 0:
        print("Проигрыш!")
        break
