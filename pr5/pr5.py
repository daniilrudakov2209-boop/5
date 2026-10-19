print("Цикл for задание 1: ")
for i in range(1, 11):
    print(i)


print("Цикл for задание 2: ")
for i in range(2, 51, 2):
    print(i)


print("Цикл for задание 3: ")
for i in range(10, 0, -1):
    print(i)


print("Цикл for задание 4: ")
n_for4 = int(input("Введите число: "))
s_for4 = 0

for i in range(1, n_for4 + 1):
    s_for4 += i

print("Сумма:", s_for4)


print("Цикл for задание 5: ")
n_for5 = int(input("Введите число: "))
factorial_for5 = 1

for i in range(1, n_for5 + 1):
    factorial_for5 *= i

print("Факториал:", factorial_for5)


print("Цикл for задание 6: ")
n_for6 = int(input("Введите число: "))

for i in range(1, 11):
    print(n_for6, "*", i, "=", n_for6 * i)


print("Цикл for задание 7: ")
numbers_for7 = [3, -2, 5, 0, -7, 8]
count_for7 = 0

for number in numbers_for7:
    if number > 0:
        count_for7 += 1

print("Количество положительных чисел:", count_for7)


print("Цикл for задание 8: ")
text_for8 = input("Введите строку: ").lower()
vowels_for8 = "аеёиоуыэюяaeiou"
count_for8 = 0

for letter in text_for8:
    if letter in vowels_for8:
        count_for8 += 1

print("Количество гласных:", count_for8)


print("Цикл for задание 9: ")
numbers_for9 = [4, 12, 7, 25, 3, 18]
largest_for9 = numbers_for9[0]

for number in numbers_for9:
    if number > largest_for9:
        largest_for9 = number

print("Наибольший элемент:", largest_for9)


print("Цикл for задание 10: ")
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print()