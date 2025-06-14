"""Черепаха выполнила следующую программу:

Налево 255
Повтори 3 [Налево 30 Повтори 4 [Вперёд 10 Налево 90]]

Определите, общее количество различных точек с целочисленными координатами,
которые будут находиться на пересечении только двух фигур, полученных при выполнении данной программы.
Точки на линиях учитывать не следует."""

from turtle import *

tracer(0)
t = Turtle()
t.pensize(3)
t.color('blue')
k = 35
screensize(1000, 1000)

t.home()

t.lt(225)
for i in range(3):
    t.lt(30)
    for j in range(4):
        t.fd(10 * k)
        t.lt(90)
for x in range(-20, 20):
    for y in range(-20, 20):
        t.pu()
        t.goto(x * k, y * k)
        t.pd()
        t.dot(3)

done()
print(30 + 26)

