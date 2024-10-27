from itertools import *

n = '18 278 378 467 567 645 72345 8123'
p = 'АВГ БГД ВАЕЛ ГАБЕК ДБК ЕВГ КГД ЛВ'
p = {x[0]: set(x[1:]) for x in p.split()}

for k in permutations('АБВГДЕКЛ'):
    s = n
    for x, y in zip('12345678', k):
        s = s.replace(x, y)
    s = {x[0]: set(x[1:]) for x in s.split()}
    if s == p:
        print('1 2 3 4 5 6 7 8')
        print(*k)
