# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# 8-5+2-1
# Вывод
# 4

# s = input("Введите выражение: ")
# sum = 0
# if s[0] == "-":
#     sum = int(s[1])*(-1)
# elif s[0] == "+":
#     sum = int(s[1])
# else:
#     sum = int(s[0])
#
# for i in range(len(s)):
#     if s[i] == "-":
#         sum -= int(s[i+1])
#     if s[i] == "+":
#         sum += int(s[i+1])
# print(f"Ответ: {sum}")


# Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)
#
# Формат ввода
# Вводится строка.
#
# Формат вывода
# Выведите слова из строки по одному.
#
# Пример 1
# Hello, world!
# Вывод
# Hello,
# world!
# Пример 2
# Ввод
#
# My heart in the Highland
# Вывод
# My
# heart
# in
# the
# Highland

# Метод строк? Это же не он?

# s = input("Введите текст: \n").split()
# print(type(s))
# for i in range(len(s)):
#     print(s[i])

# НЕОБЯЗАТЕЛЬНЫЕ РЕШАЮ
# Задача 26:
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def exponentiation(a, b):
#     e = a
#     for _ in range(b-1):
#         e = e*a
#     return e
#
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# expo = exponentiation(a, b)
# print(expo)


# Задача 28:
# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4
# Не поняла задания (6-_- )
def sum(a, b):
    sum = a+b
a = int(input("Введите число: "))
b = int(input("Введите число: "))
print(sum(a, b))