"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать
функцию input().
"""

first_list = list(input('Введите абстрактную строку\n>>>:'))
list_length = len(first_list) // 2
position = 0
count = 0

while count < list_length:
    first_list.insert(position, first_list[position+1])
    first_list.pop(position+2)
    position+=2
    count+=1

print(first_list)

