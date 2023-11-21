# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate
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
def ping_ip_addresses(list_of_ips):
    list_of_ips=convert_ranges_to_ip_list(list_of_ips)
    test_result = {'Reachable': [], 'Unreachable': []}
    for ip in list_of_ips:
        ping_check = subprocess.run(['ping', '-c', '3', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if ping_check.returncode == 0:
            test_result['Reachable'].append(ip)
        else:
            test_result['Unreachable'].append(ip)
    return(test_result)

if __name__ == "__main__":
    print(tabulate(ping_ip_addresses(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132'])))
    #print(tabulate(ping_ip_addresses(['192.168.74.1', '127.0.0.1', 'ya.ru', '192.168.12.1' '192.168.11.1']), headers='keys'))

#Сам себя не похвалишь, конечно, никто не похвалит. Но я боженька