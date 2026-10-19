print("Цикл while задание 1: ")
i_while1 = 1

while i_while1 <= 10:
    print(i_while1)
    i_while1 += 1


print("Цикл while задание 2: ")
total_while2 = 0
number_while2 = int(input("Введите число (0 для остановки): "))

while number_while2 != 0:
    total_while2 += number_while2
    number_while2 = int(input("Введите число (0 для остановки): "))
print("Сумма:", total_while2)


print("Цикл while задание 3: ")
n_while3 = int(input("Введите натуральное число: "))
count_while3 = 0

while n_while3 > 0:
    count_while3 += 1
    n_while3 //= 10
print("Количество цифр:", count_while3)


print("Цикл while задание 4: ")
n_while4 = int(input("Введите натуральное число: "))
total_while4 = 0

while n_while4 > 0:
    digit_while4 = n_while4 % 10
    total_while4 += digit_while4
    n_while4 //= 10
print("Сумма цифр:", total_while4)


print("Цикл while задание 5: ")
n_while5 = int(input("Введите натуральное число: "))
reversed_number_while5 = 0

while n_while5 > 0:
    digit_while5 = n_while5 % 10
    reversed_number_while5 = reversed_number_while5 * 10 + digit_while5
    n_while5 //= 10
print("Обратное число:", reversed_number_while5)


print("Цикл while задание 6: ")
n_while6 = int(input("Введите число: "))
power_while6 = 1

while power_while6 <= n_while6:
    print(power_while6)
    power_while6 *= 2


print("Цикл while задание 7: ")
correct_password_while7 = "123"
password_while7 = input("Введите пароль: ")

while password_while7 != correct_password_while7:
    print("Неверный пароль!")
    password_while7 = input("Попробуйте ещё раз: ")
print("Пароль верный!")


print("Цикл while задание 8: ")
a_while8 = int(input("Введите первое число: "))
b_while8 = int(input("Введите второе число: "))

while b_while8 != 0:
    a_while8, b_while8 = b_while8, a_while8 % b_while8

print("НОД:", a_while8)


print("Цикл while задание 9: ")
n_while9 = int(input("Введите число: "))
a_while9 = 0
b_while9 = 1

while a_while9 <= n_while9:
    print(a_while9)
    a_while9, b_while9 = b_while9, a_while9 + b_while9


print("Цикл while задание 10: ")
import random

secret_while10 = random.randint(1, 100)
attempts_while10 = 0

guess_while10 = int(input("Угадайте число от 1 до 100: "))

while guess_while10 != secret_while10:
    attempts_while10 += 1

    if guess_while10 < secret_while10:
        print("Больше")
    else:
        print("Меньше")

    guess_while10 = int(input("Попробуйте ещё раз: "))

attempts_while10 += 1

print("Правильно! Вы угадали.")
print("Количество попыток:", attempts_while10)