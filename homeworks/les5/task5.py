# -*- coding: utf8 -*-
"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import json


new_list = [1, 5, 653, 67, 34, 0, 65]
with open("task5.json", "w") as task5:
    json.dump(new_list, task5)

with open("task5.json") as task5:
    result_list = json.load(task5)

print(sum(result_list))




