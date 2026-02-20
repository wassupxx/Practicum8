order_number=1
found = False
while not found:
    number = input("Введите номер билета: ")
    ticket = list(number)
    first_half = ticket[:len(ticket) // 2]
    second_half = ticket[len(ticket) // 2:]
    summary_first = 0
    summary_second = 0
    if len(number) % 2 == 1:
        print("Номер билета должен содержать четное кол-во цифр.")
        continue
    for index in range((len(first_half) // 2)):
        summary_first += int(first_half[index])
    for index in range((len(second_half) // 2)):
        summary_second += int(second_half[index])
        if summary_first == summary_second:
            found = True
            print(f"Счастливый билет найден! Порядковый номер: {order_number}")
            break
        else:
            order_number += 1
