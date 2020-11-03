"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
 вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

new_file = open("first_file.txt", "a")
new_line = []
while True:
    line = input("Введите текст\n")
    if line == '':
        break
    new_line.append(line + "\n")

new_file.writelines(new_line)
new_file.close()




