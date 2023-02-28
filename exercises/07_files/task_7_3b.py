# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
spis = []
with open('CAM_table.txt') as f:
    for line in f:
        data = line.split()
        if len(data) > 1 and data[0].isdigit():
            line_list = [int(data[0]), data[1], data[3]]
            spis.append(line_list)
    user_vlan = input('Введите номер влана: \n')
    for i in sorted(spis):
        if int(user_vlan) == i[0]:
            print('{:<9}{:<20}{}'.format(i[0], i[1], i[2]))
    else:
        print('А вот хуй. Нету такого влана блядь. Я всё облазил')