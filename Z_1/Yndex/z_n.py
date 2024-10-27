from itertools import *


n = '1567 234 3247 4235 514 617 7136'
p = "AFDE BDC CBEG DFAB EACG FAD GEC"
p = {x[0]: set(x[1:]) for x in p.split()}

for k in permutations('ABCDEFG'):
    s = n
    for x, y in zip('1234567', k):
        s = s.replace(x, y)
    s = {x[0]: set(x[1:]) for x in s.split()}
    if s == p:
        print('1 2 3 4 5 6 7')
        print(*k)