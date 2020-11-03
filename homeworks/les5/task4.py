"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

old_list = open("task4.txt")
new_list = open("task4_new.txt", "a")
new_dict = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре '}

for line in old_list:
    key, value = line.split(' - ')
    new_line = [new_dict.get(int(value)), value]
    new_list.write(' - '.join(new_line))

old_list.close()
new_list.close()