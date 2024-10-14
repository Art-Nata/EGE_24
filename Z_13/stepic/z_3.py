from ipaddress import *

net = ip_network('116.29.170.89/255.255.255.224', 0)
print(net, net.num_addresses)
count = 0
for adr in net:
    #x = f'{adr:b}'.zfill(32)
    x = bin(int(adr))[2:].zfill(32) #одинаковый результат
    print(x[:16], x[16:])
    if x[:16].count('1') >= x[16:].count('1'):
        count += 1
print(count)