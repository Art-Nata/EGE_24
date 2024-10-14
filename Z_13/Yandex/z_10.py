"""Сеть задана IP-адресом 112.208.0.0 и сетевой маской 255.255.128.0.

Сколько в этой сети ІР-адресов, для которых количество единиц в двоичной записи IP-адреса кратно 11?
В ответе укажите только число."""

from ipaddress import ip_network

ip_net = '112.208.0.0'
mask = '255.255.128.0'
net = ip_network('/'.join([ip_net, mask]))
count = 0
for ip_adr in net:
    ip_bin = bin(int(ip_adr))[2:]

    if ip_bin.count('1') % 11 == 0:
        count += 1
print(count)