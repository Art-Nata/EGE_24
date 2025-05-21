from itertools import *


n = '1457 2346 3247 412356 5146 6245 713'
k = 'ACEF BFDG CAFG DEFB EAFD FACBDE GCB'

k = {x[0]: set(x[1:]) for x in k.split()}

