# Задача №31.
# Последовательностью Фибоначчи называется
# последовательность чисел a[0], a[1], ..., a[n], ..., где
# a[0] = 0, a[1] = 1, a[k] = a[k-1] + a[k-2] (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# Задание необходимо решать через рекурсию

import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = int(input("Введите число: "))

start = time.perf_counter()
print(f"Через рекурсию: {fib(n)}")
end = time.perf_counter()
first_time = end - start
print(first_time)

zero = 0
first = 1
for el in range(2, n + 1):
    second = zero + first
    zero, first = first, second
start = time.perf_counter()
print(f"Через цикл: {second}")
end = time.perf_counter()
second_time = end - start
print(second_time)

print(first_time / second_time)


# Задача №33.
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

marks_list = [int(input()) for _ in range(int(input("ведите кол-во оценок: ")))]
maxx = marks_list[0]
minn = marks_list[0]
for el in marks_list:
    if el < minn:
        minn = el
    if el > maxx:
        maxx = el
for i in range(0, len(marks_list)):
    if marks_list[i] == maxx:
        marks_list[i] = minn
print(marks_list)


# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def simple_number(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return "No"
    return "Yes"
print(simple_number(11))

# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3