# -*- coding: utf8 -*-
"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
"""
import json

profit_list = {}
delta_profit = {}
count = 0
all_profit = 0
with open("task7.txt") as new_file:
    for line in new_file:
        firm_name, asset, revenue, cost = line.split(' ')
        profit = int(revenue) - int(cost)
        profit_list[firm_name] = profit
        if profit > 0:
            count += 1
            all_profit += profit
delta_profit["average_profit"] = profit / count
busness_report = [profit_list, delta_profit]

with open("task7.json", "a") as new_json:
    json.dump(busness_report, new_json)
