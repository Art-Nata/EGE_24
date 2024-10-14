"""Для узла с IP адресом 158.116.11.146 адрес сети равен 158.116.0.0.
Для скольких различных значений маски это возможно?

Ответ 7"""

ip_comp = '158.116.11.146'
ip_net = '158.116.0.0'

print(".".join(bin(int(x))[2:].zfill(8) for x in ip_comp.split(".")), 'ip-адрес узла')
print('.'.join(["********"] * 4), 'маска')
print(".".join(bin(int(x))[2:].zfill(8) for x in ip_net.split(".")), 'адрес сети')