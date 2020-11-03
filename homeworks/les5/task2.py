"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке
"""

try:
    with open("task2.txt") as new_file:
        count = 0
        for line in new_file:
            count += 1
            print('Строка номер:', count, '; Количество слов:', len(line.split(' ')))
    print('Всего строк', count)
except IOError:
    print('Файл не найден')
