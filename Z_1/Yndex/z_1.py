from itertools import *


n = '1356 26 314 436 51 6124'
p = 'AB BACE CBD DCE FE EDBF'
p = {x[0]: set(x[1:]) for x in p.split()}

for k in permutations('ABCDEF'):
    s = n
    for x, y in zip('123456', k):
        s = s.replace(x, y)

    s = {x[0]: set(x[1:]) for x in s.split()}
#    if s['A'] == {'B'}:
#        print(s)
    if s == p:
        print('1 2 3 4 5 6')
        print(*k)
