# # Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# # Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# # В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# # 5
# # 1 2 3 4 5
# # 3
# # -> 1


list_1 = [_ for _ in range(1, int(input("Введите размер массива: "))+1)]
print(list_1)
x = int(input("Введите чило: "))
count = 0
for j in range(len(list_1)):
    if list_1[j] == x:
        count += 1
print(f"Число есть в списке - {x in list_1}")
print(f"Кол-во элементов: {count}")


# from random import randint
# list_1 = [i for i in range(1, int(input("Введите размер массива: "))+1)] # заполнение массива подряд
# print(list_1)
# list_2 = [randint(1, 20) for _ in range(int(input("Сколько вы хотите доп. элементов? ")))] # заполнение рандомно
# list_3 = list_1 + list_2 # сложение списков
# print(list_3)
# x = 1
# while x != 0:
#     count = 0
#     x = int(input("Введите число или 0: "))
#     for j in range(len(list_3)):
#         if list_3[j] == x:
#             count += 1
#     print(count)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


# 5
#     1 2 3 4 5
#     6
#     -> 5

list_1 = [i for i in range(1, int(input("Введите размер массива: "))+1)]
print(list_1)
x = int(input("Введите x: "))
list_2 = []
for j in range(len(list_1)):
    if list_1[j] - 1 == x or list_1[j] + 1 == x:
        list_2.append(list_1[j])
if x > list_1[-1]:
    list_2.append(list_1[-1])
    list_2.insert(1, x)
elif x < list_1[0]:
    list_2.append(list_1[0])
    list_2.insert(0, x)
else:
    list_2.insert(1, x)
print(*list_2, sep = " < ")


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, 
# что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# ноутбук
#     12

# ОГРОМНОЕ РЕШЕНИЕ!!!

eng = {
1: ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "L", "l", "N", "n", "S", "s", "T", "t", "R", "r"), 
2:("D", "d", "G", "g"), 
3: ("B", "b", "C", "c", "M", "m", "P", "p"), 
4: ("F", "f", "H", "h", "V", "v", "W", "w", "Y", "y"),  
5: ("K", "k"), 
8: ("J", "j", "X", "x"), 
10: ("Q", "q", "Z", "z")
}

ru = {
1: ("А", "а", "В", "в", "Е", "е", "И", "и", "Н", "н", "О", "о", "Р", "р", "С", "с", "Т", "т"), 
2: ("Д", "д", "К", "к", "Л", "л", "М", "м", "П", "п", "У", "у"), 
3: ("Б", "б", "Г", "г", "Ё", "ё", "Ь", "ь", "Я", "я"), 
4: ("Й", "й", "Ы", "ы"),  
5: ("Ж", "ж", "З", "з", "Х", "х", "Ц", "ц", "Ч", "ч"), 
8: ("Ш", "ш", "Э", "э", "Ю", "ю"), 
10:("Ф", "ф", "Щ", "щ", "Ъ", "ъ")
}
print(type(ru))
string = input("Введите слово\n")
sum = 0
for i in range(len(string)):
    if string[i] in eng[1]:
        sum += 1
    elif string[i] in eng[2]:
        sum += 2
    elif string[i] in eng[3]:
        sum += 3
    elif string[i] in eng[4]:
        sum += 4
    elif string[i] in eng[5]:
        sum += 5
    elif string[i] in eng[8]:
        sum += 8
    elif string[i] in eng[10]:
        sum += 10
    else:
        break

for i in range(len(string)):
    if string[i] in ru[1]:
        sum += 1
    elif string[i] in ru[2]:
        sum += 2
    elif string[i] in ru[3]:
        sum += 3
    elif string[i] in ru[4]:
        sum += 4
    elif string[i] in ru[5]:
        sum += 5
    elif string[i] in ru[8]:
        sum += 8
    elif string[i] in ru[10]:
        sum += 10
    else:
        break
print(sum)