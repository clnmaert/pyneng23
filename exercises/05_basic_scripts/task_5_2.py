# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
enterip = input('Введити ваш айпи в формате 10.1.1.0/24: \n')
userip = enterip.split('/')[0].split('.')
usermask = int(enterip.split('/')[-1])
binmask = ('1' * usermask + '0' * (32 - usermask))
template = '''
Network:
{:<8}  {:<8}  {:<8}  {:<8}
{:08b}  {:08b}  {:08b}  {:08b}  

Mask:
/{:<8}
{:<8} {:<8} {:<8} {:<8}
{:<8} {:<8} {:<8} {:<8}
'''
print(template.format(
    userip[0], userip[1], userip[2], userip[3],
    int(userip[0]), int(userip[1]), int(userip[2]), int(userip[3]),
    usermask,
    int(binmask[0:8], 2), int(binmask[8:16], 2), int(binmask[16:24], 2), int(binmask[24:], 2),
    binmask[0:8], binmask[8:16], binmask[16:24], binmask[24:]
))
print('8========================================о   (_*_)')
print('Ну какой же я молодец такие темплейты забубенивать')