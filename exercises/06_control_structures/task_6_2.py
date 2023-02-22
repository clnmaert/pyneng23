# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
userip = input('Ввидите ваш айпи: \n')
userip_list = userip.split('.')

if 1 < int(userip_list[0]) < 223:
    print('unicast')
elif 1 < int(userip_list[0]) < 239:
    print('multicast')
elif userip == '255.255.255.255':
    print('local broadcast')
elif userip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
print('=' * 30)
print('Ай да я! Ай да молодец')
print('!' * 30)