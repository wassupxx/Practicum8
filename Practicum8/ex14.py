hint = input()
word = input().lower()
print("\n" * 25)
guess_word = ["*"] * len(word)
attempts = 10
print(hint)
while attempts > 0:
    choice = input("Буква или слово? (0 — буква, 1 — слово): ")
    if choice == "0":
        letter = input()
        if letter in word:

            for placement in range(len(word)):
                if word[placement] == letter:
                    guess_word[placement] = letter
            print(" ".join(guess_word))
        else:
            print(" ".join(guess_word))
    elif choice == "1":
        test_word = input()
        if word == test_word:
            guess_word = word
            print("Победа!")
            break
        else:
            break
    attempts -= 1
    if attempts == 0:
        break
    if "*" not in guess_word:
        print("Победа!")
        break
if "*" in guess_word:
    print("Проигрыш!", f"Правильное слово: {word}")
