"""Черепахе был дан для исполнения следующий алгоритм:

Направо 90
Повтори 3 [Направо 45 Вперёд 10 Направо 45]
Направо 315 Вперёд 10
Повтори 2 [Направо 90 Вперёд 10].
Определите, сколько точек с целочисленными координатами будут находиться внутри области,
которая ограничена линией, заданной алгоритмом. Точки на линии учитывать не следует."""


from turtle import *

tracer(0)
t = Turtle()
t.pensize(3)
t.color('blue')
k = 30
screensize(1000, 1000)

t.home()
t.rt(90)
for i in range(3):
    t.rt(45)
    t.fd(10 * k)
    t.rt(45)
t.rt(315)
t.fd(10 * k)
for i in range(2):
    t.rt(90)
    t.fd(10 * k)

for x in range(-20, 20):
    for y in range(-20, 20):
        t.pu()
        t.goto(x * k, y * k)
        t.pd()
        t.dot(3)

done()
print(29 * 7)


