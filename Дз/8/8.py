# Напишите функцию read_last(lines, file),
# которая будет открывать определенный файл file и выводить на печать
# построчно последние строки в количестве lines (на всякий случай проверим,
# что задано положительное целое число). Протестируем функцию
# на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

def read_last(lines, file):
    if lines != 0:
        line = file.readlines()[-lines:]
        for el in line:
            print(el)

n = int(input("Введите кол-во строк: "))
if n >= 0 and n % 1 == 0:
    with open('article.txt', 'r', encoding='utf-8') as file:
        read_last(n, file)
else:
    print("Вы указали неверное значение")


# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file),
# которая записывает в файл result.txt слово, имеющее максимальную длину
# (или список слов, если таковых несколько).
def longest_words(file):
    line = file.read().splitlines()
    max = len(line[0])
    result = []

    for i in range(len(line)):
        if len(line[i]) > max:
            result = []
            result.append(line[i])
            max = len(line[i])
        elif len(line[i]) == max:
            result.append(line[i])
    write_word(result)
def write_word(result):
    with open('result.txt', 'w', encoding='utf-8') as res:
        for el in result:
            res.write(el)


with open('article.txt', 'r', encoding='utf-8') as file:
    longest_words(file)