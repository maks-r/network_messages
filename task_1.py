'''
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
(Внимание! Аргументом сабпроцесcа должен быть список, а не строка!!! Для уменьшения времени работы скрипта при проверке
нескольких ip-адресов, решение необходимо выполнить с помощью потоков)
'''
import platform
import subprocess
from ipaddress import ip_address
import time
from threading import Thread


res = {'Доступные узлы: ': '', 'Недоступные узлы: ': ''}
hosts = ['192.168.0.1', 'mail.ru', 'gb.ru', 'yandex.ru', '192.168.8.1', 'abracadabra',
         '1.1.1.1.22', '192.168.0.0/13', 'gb.comru']
is_win = platform.system().lower() == 'windows'
param = '-n' if is_win else '-c'


def check_ip(host):
    try:
        check = ip_address(host)
    except ValueError:
        raise Exception('Ошибка!!! Неправильный ip!')
    return check


def host_ping(hosts, is_print=False):
    for host in hosts:
        try:
            ip = check_ip(host)
        except Exception as e:
            print(f'{host} - {e} - доменное имя')
            ip = host

        command = ['ping', param, '1', str(ip)]
        response = subprocess.run(command, shell=is_win, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if response.returncode == 0:
            res['Доступные узлы: '] += f'{ip}\n'
            res_str = f'{ip} - Узел доступен'
        else:
            res['Недоступные узлы: '] += f'{ip}\n'
            res_str = f'{ip} - Узел не доступен'
        if not is_print:
            print(res_str)
    if is_print:
        return res


def clock(interval):
    while True:
        print(interval)
        print(f"Текущее время: {time.ctime()}")
        time.sleep(interval)
        break


if __name__ == '__main__':
    start = time.time()
    host_ping(hosts)
    end = time.time()
    THR = Thread(target=clock, args=(1,))
    THR.daemon = False
    THR.start()
    THR.join()
    print(f"Время окончания программы: {time.ctime()}")
    print(f'Общее время: {end - start}')
