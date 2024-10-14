"""Сеть задана IP-адресом 10.112.0.0 и маской сети 255.248.0.0.

Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса кратно 3?

В ответе укажите только число."""

from ipaddress import ip_network

ip_net = '10.112.0.0'
mask = '255.248.0.0'
net = ip_network('/'.join([ip_net, mask]))
count = 0
for ip_adr in net:
    ip_bin = bin(int(ip_adr))[2:]

    if ip_bin.count('1') % 3 == 0:
        count += 1
print(count)