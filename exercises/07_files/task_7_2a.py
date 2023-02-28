# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["alias", "duplex", "configuration"]
with open('C:/Users/maert/PycharmProjects/pyneng23/exercises/07_files/config_sw1.txt') as f:
    for line in f:
        words = line.split()
        words_intersect = set(words) & set(ignore)
        if not line.startswith('!') and not words_intersect:
            print(line.rstrip())

#хуйня 3
        '''for word in ignore:
            if line.startswith('!') or (word in line):
                break
            else:
                print(line.rstrip())'''

#хуйня 2
'''        if not line.startswith('!'):
            for word in ignore:
                if word in line:
                    break
                else:
                    print(line.rstrip())'''
