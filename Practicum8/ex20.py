def number_to_words(n):
    if n == 0:
        return "ноль"
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять",
              "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
              "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят",
            "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот",
               "семьсот", "восемьсот", "девятьсот"]

    def convert_under_1000(num):
        result = ""
        if num >= 100:
            result += hundreds[num // 100] + " "
            num %= 100
        if 1 <= num <= 19:
            result += units[num]
        elif num >= 20:
            result += tens[num // 10]
            if num % 10 != 0:
                result += " " + units[num % 10]
        return result.strip()

    result = ""

    millions = n // 1_000_000
    if millions:
        if millions == 1:
            million_word = "миллион"
        elif 2 <= millions % 10 <= 4 and millions % 100 not in (12, 13, 14):
            million_word = "миллиона"
        else:
            million_word = "миллионов"
        result += convert_under_1000(millions) + " " + million_word + " "

    thousands = (n // 1_000) % 1_000
    if thousands:
        if thousands == 1 and thousands % 100 != 11:
            thousand_word = "тысяча"
        elif 2 <= thousands % 10 <= 4 and thousands % 100 not in (12, 13, 14):
            thousand_word = "тысячи"
        else:
            thousand_word = "тысяч"
        result += convert_under_1000(thousands) + " " + thousand_word + " "

    remainder = n % 1_000
    if remainder:
        result += convert_under_1000(remainder)

    return result.strip()
n = int(input())
print(number_to_words(n))
