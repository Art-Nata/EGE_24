from ipaddress import *

# print('.'.join(f'{x:08b}' for x in [122, 168, 11, 45])) #получение двоичного IP-адреса
#
# print(f'{144:08b}') #печать десятичного числа в двоичном виде
#
# print(bin(45)[2:])

#x = f'{adr:b}'.zfill(32) #другой способ получения двоичного значения
#dv = bin(int(ad))[2:].zfill(32)



net1 = ip_network('19.168.34.90/5', 0)
net2 = ip_network('192.168.34.90/255.0.0.0', 0)

print(net1, net2)

print(net1, net1.num_addresses) # количество всех адресов в сети ( и 0000 и 1111)
print(net1.netmask)


