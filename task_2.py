'''
2. Написать функцию host_range_ping() (возможности которой основаны на функции из примера 1) для перебора ip-адресов
из заданного диапазона. Меняться должен только последний октет каждого адреса. По результатам проверки должно
выводиться соответствующее сообщение.
'''


from ipaddress import ip_address
from task_1 import host_ping


def host_range_ping(first_ip, last_ip, is_print=False):
    try:
        start_ip = ip_address(first_ip)
        end_ip = ip_address(last_ip)
        start_ip, end_ip = sorted((start_ip, end_ip))
    except Exception:
        print('Ошибка!!! Указан некорректный ip')
        return
    ip_list = []

    while start_ip <= end_ip:
        ip_list.append(start_ip)
        start_ip += 1

    return [i for i in host_ping(ip_list, is_print)]


if __name__ == '__main__':
    host_range_ping('192.168.0.1', '192.168.0.11')


