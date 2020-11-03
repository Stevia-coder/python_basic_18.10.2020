"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
 выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

time = input('Введите пожалуйста время в секундах\n>>>:')
seconds = int(time) % 60
time = int(time) // 60
minutes = time % 60
hours = int(time) // 60
full_time = f'{hours}:{minutes}:{seconds}'
print(full_time)
