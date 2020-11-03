"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
 вывести фамилии этих сотрудников.
 Выполнить подсчет средней величины дохода сотрудников.
"""

staff = 0
salary = 0
try:
    with open("task3.txt") as new_file:
        for line in new_file:
            key, value = line.split(':')
            staff += 1
            salary += int(value)
            if int(value) < 20000:
                print(key)
except IOError:
    print('Файл не найден')
print(salary / staff)


