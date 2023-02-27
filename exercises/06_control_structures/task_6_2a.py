# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
userip = input('Ввидите ваш айпи: \n')
userip_list = userip.split('.')

correct_ip = False
while not correct_ip:
    if not userip.replace('.', '').isdigit():
        print('Неправильный IP-адрес')
    elif not userip.count('.') == 3:
        print('Неправильный IP-адрес')
    elif len(userip_list) != 4:
        print(len(userip_list))
        print('Неправильный IP-адрес')
    elif int(userip_list[0]) not in range(256):
        print('Неправильный IP-адрес')
    else:
        correct_ip = True
        continue
    userip = input('Ввидите ваш айпи: \n')

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