import math

n = 1280 * 720
i = math.log(4096, 2)
v = 96468992
t = 280
vol = v * t
vol1 = n * i
print(i, vol / vol1)