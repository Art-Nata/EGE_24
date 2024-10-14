from ipaddress import *

net = ip_network('249.0.33.87/255.252.0.0', 0)
count = 0
for adr in net:
    x = f'{adr:b}'.zfill(32)
    #x = bin(int(adr))[2:].zfill(32) #одинаковый результат
    if 2 * x[:16].count('1') < x[16:].count('1'):
        count += 1
print(count)