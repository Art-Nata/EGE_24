print('w x y z f')
for w in (0, 1):
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                f = not (not(x <= (not w)) and z) and (not (w <= z)) and (x <= (not z))
                print(w, x, y, z, f)

