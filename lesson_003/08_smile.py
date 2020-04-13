# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random

sd.resolution = (1100, 600)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
x = sd.random_point()


def smile():
    x = sd.random_point()
    sd.ellipse(x, sd.get_point(x.x+100, x.y+50), width=2)
    center = sd.get_point(x.x+37.5, x.y+37.5)
    center_2 = sd.get_point(x.x+65, x.y+37.5)
    sd.circle(center, 4)
    sd.circle(center_2, 4)
    point_list = [sd.get_point(x.x+25, x.y+25),
                  sd.get_point(x.x+35, x.y+20.5),
                  sd.get_point(x.x+55, x.y+20.5),
                  sd.get_point(x.x+75, x.y+25)
                  ]
    sd.lines(point_list, width=1)

for i in range(10):
    smile()


sd.pause()
