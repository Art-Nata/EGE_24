"""Ишимов М.Тема: Маска подсети(Маска подсети)
Сеть задана IP-адресом 87.226.26.72 и маской сети 255.255.255.252.
Сколько в этой сети IP-адресов, у которых количество нулей в двоичной записи IP-адреса чётно?

В ответе укажите только число."""

from ipaddress import ip_network

ip_net = '87.226.26.72'
mask = '255.255.255.252'
net = ip_network('/'.join([ip_net, mask]))
count = 0
for ip_adr in net:
    ip_bin = bin(int(ip_adr))[2:]

    if ip_bin.count('0') % 2 == 0:
        #print(len(bin(int(ip_adr))), ip_1, ip_2)
        count += 1
print(count)