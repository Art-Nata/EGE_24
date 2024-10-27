from itertools import *


n = '12467 21357 325 4156 52346 6145 712'
p = 'АБВГ БАВЕЖ ВАБГ ГАВЕД ДГЕ ЕЖБГД ЖБЕ'
p = {x[0]: set(x[1:]) for x in p.split()}
for k in permutations('АБВГДЕЖ'):
    s = n
    for x, y in zip('1234567', k):
        s = s.replace(x, y)
    s = {x[0]: set(x[1:]) for x in s.split()}
    if s == p:
        print('1 2 3 4 5 6 7')
        print(*k)
