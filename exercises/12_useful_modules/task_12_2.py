# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import subprocess

def convert_ranges_to_ip_list(bunch_of_ips):
    result = []
    for i in bunch_of_ips:
        if '-' in i:
            if i.count('.') == 6:
                firstip = i.split('-')[0]
                lastip = i.split('-')[-1]
                base_ip = firstip.split('.')
                first_three_octets = f'{base_ip[0]}.{base_ip[1]}.{base_ip[2]}.'
                #print(f'firstip {firstip}\nlastip {lastip}\nfirst_three_octets {first_three_octets}')
                #print(f'first {firstip.split[-1]}\nlast {lastip.split[-1]}')
                for r in range(int(firstip.split('.')[-1]), int(lastip.split('.')[-1])+1):
                    result.append(f'{first_three_octets}{r}')
            else:
                base_ip = i.split('.')
                last_octet_range = base_ip[-1]
                first_three_octets = f'{base_ip[0]}.{base_ip[1]}.{base_ip[2]}.'
                for s in range(int(last_octet_range[0]), int(last_octet_range[-1])+1):
                    result.append(f'{first_three_octets}{s}')
        else:
            result.append(i)
    return result
if __name__ == "__main__":
    print(convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']))

#ai da ya!