from ipaddress import *

for a in range(256):
    net = ip_network(f'32.0.{a}.5/255.255.240.0', 0)
    for adr in net:
        z = f'{adr:b}'.zfill(32)
        if z[:16].count('1') > z[16:].count('1'):
            break
    else:
        print(a)

