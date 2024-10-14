from ipaddress import *

net = ip_network('105.224.200.224/255.255.255.224', 0)
count = 0
for adr in net:
    x = f'{adr:b}'.zfill(32)
    #x = bin(int(adr))[2:].zfill(32) #одинаковый результат
    if x.count('1') % 4 == 0:
        count += 1
print(count)