# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1100, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(200, 200)
r = 50
for _ in range(3):
    sd.circle(center_position=point, radius=r)
    r += 5

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble_draw(x=100, y=100, radius=50, n_bubble = 1, step_r=0):
    point = sd.get_point(x, y)
    for _ in range(n_bubble):
        sd.circle(center_position=point, radius=radius)
        radius += step_r

bubble_draw(n_bubble=11, step_r=5)
# Нарисовать 10 пузырьков в ряд

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        bubble_draw(x=x, y=y)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
def bubble_random_draw(n_bubble = 100):
    for _ in range(n_bubble):
        point = sd.random_point()
        radius = random.randint(15, 75)
        col = sd.random_color()
        sd.circle(center_position=point, radius=radius, color=col)

bubble_random_draw()
sd.pause()


