from ipaddress import *

for masc in range(16, 25): #количество единиц в маске
    net = ip_network(f'199.59.129.3/{masc}', 0)

    for adr in net:
        x = f'{adr:b}'.zfill(32)
        if x[:16].count('1') < x[16:].count('1'):
            break
    else:
        print(net.netmask)