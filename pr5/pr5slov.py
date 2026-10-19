print("Словари задание 1: ")
grades_dict1 = {
    "Анна": 5,
    "Иван": 4,
    "Мария": 3
}

print("Оценка Анны:", grades_dict1["Анна"])


print("Словари задание 2: ")
students_dict2 = {
    "Анна": 5,
    "Иван": 4,
    "Мария": 3
}

students_dict2["Пётр"] = 5
students_dict2["Иван"] = 5
del students_dict2["Мария"]

print(students_dict2)


print("Словари задание 3: ")
person_dict3 = {
    "имя": "Иван",
    "возраст": 18,
    "город": "Москва"
}

key_dict3 = input("Введите ключ: ")

if key_dict3 in person_dict3:
    print(person_dict3[key_dict3])
else:
    print("Нет такого ключа")


print("Словари задание 4: ")
data_dict4 = {
    "яблоко": 50,
    "банан": 80,
    "апельсин": 70
}

print("Ключи:", list(data_dict4.keys()))
print("Значения:", list(data_dict4.values()))
print("Количество пар:", len(data_dict4))


print("Словари задание 5: ")
prices_dict5 = {
    "Хлеб": 60,
    "Молоко": 90,
    "Сыр": 350
}

for product, price in prices_dict5.items():
    print(product, "-", price, "руб.")


print("Словари задание 6: ")
prices_dict6 = {
    "Хлеб": 60,
    "Молоко": 90,
    "Сыр": 350,
    "Яблоки": 120
}

total_dict6 = 0
most_expensive_dict6 = ""
max_price_dict6 = -1

for product, price in prices_dict6.items():
    total_dict6 += price

    if price > max_price_dict6:
        max_price_dict6 = price
        most_expensive_dict6 = product

print("Сумма всех цен:", total_dict6)
print("Самый дорогой товар:", most_expensive_dict6)
print("Его цена:", max_price_dict6)


print("Словари задание 7: ")
text_dict7 = input("Введите строку: ")
symbols_dict7 = {}

for char in text_dict7:
    if char in symbols_dict7:
        symbols_dict7[char] += 1
    else:
        symbols_dict7[char] = 1

print(symbols_dict7)


print("Словари задание 8: ")
text_dict8 = input("Введите слова через пробел: ").lower()
words_dict8 = text_dict8.split()
counts_dict8 = {}

for word in words_dict8:
    if word in counts_dict8:
        counts_dict8[word] += 1
    else:
        counts_dict8[word] = 1

print("Количество каждого слова:", counts_dict8)

most_common_dict8 = ""
max_count_dict8 = 0

for word, count in counts_dict8.items():
    if count > max_count_dict8:
        max_count_dict8 = count
        most_common_dict8 = word

if words_dict8:
    print("Самое частое слово:", most_common_dict8)
    print("Количество повторений:", max_count_dict8)
else:
    print("Строка не содержит слов")


print("Словари задание 9: ")
original_dict9 = {
    "Анна": 5,
    "Иван": 4,
    "Мария": 3
}

reversed_dict9 = {}

for key, value in original_dict9.items():
    reversed_dict9[value] = key

print(reversed_dict9)


print("Словари задание 10: ")
countries_dict10 = ["Россия", "Франция", "Италия", "Япония"]
capitals_dict10 = ["Москва", "Париж", "Рим", "Токио"]

country_capitals_dict10 = {}

for i in range(len(countries_dict10)):
    country_capitals_dict10[countries_dict10[i]] = capitals_dict10[i]

country_dict10 = input("Введите название страны: ")

if country_dict10 in country_capitals_dict10:
    print("Столица:", country_capitals_dict10[country_dict10])
else:
    print("Такой страны нет в словаре")