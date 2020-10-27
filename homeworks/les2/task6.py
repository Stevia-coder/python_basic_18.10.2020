"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
"""

#Создание реестра товаров
products = []
count = 1

while True:
    name = input('Введите название товара\n>')
    price = int(input('Введите цену товара\n>'))
    qantity = int(input('Введите количество товара\n>'))
    unit = input('Введите единицу измерения товара\n>')
    product_item = {'название': name, 'цена': price, 'количество': qantity, 'ед': unit}
    product_cort = (count, product_item)
    products.append(product_cort)
    count+=1
    stopper = input('Если хотите закончить, введите "q"\n>')
    if stopper == 'q':
        break

#print(products)
#Создание справочника с аналитикой по товарам

all_values = []
report = {}

for el in products:
    for elem in el[1:2]:
        values = []
        keys = []
        for key, value in elem.items():
            values.append(value)
            keys.append(key)
        all_values.append(values)

zip_values = list(zip(*all_values))

count = 0
while count < len(keys):
    new_dict = {keys[count]: list(zip_values[count])}
    report.update(new_dict)
    count+=1

print(report)