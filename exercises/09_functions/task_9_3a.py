# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    vlan1 = False
    with open(config_filename) as f:
        for line in f:
            if 'switchport mode access' in line:
                vlan1 = True
            elif 'interface' in line:
                interface = line.split()[-1]
            elif 'access vlan' in line:
                access_vlan = int(line.split()[-1])
                access_dict.setdefault(interface, access_vlan)
                vlan1 = False
            elif 'trunk allowed' in line:
                trunk_vlans = [int(v) for v in line.split()[-1].split(',')]
                trunk_dict.setdefault(interface, trunk_vlans)
            elif vlan1:
                access_dict.setdefault(interface, 1)
                vlan1 = False
    result_tuple = (access_dict, trunk_dict)
    return result_tuple
print(get_int_vlan_map('config_sw2.txt'))
