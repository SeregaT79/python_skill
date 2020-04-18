# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (800, 600)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

point_0 = sd.get_point(300, 300)


def draw_branches(point=[0, 0], angle=[0, 0], length=[100, 100], delta=0):
    if length[0] < 1:
        return
    v1 = sd.get_vector(start_point=point[0], angle=angle[0], length=length[0])
    v2 = sd.get_vector(start_point=point[1], angle=angle[1], length=length[1])
    v1.draw()
    v2.draw()
    next_angle = [angle[0] - delta, angle[1] + delta]
    next_length = [length[0] * 0.75, length[1] * 0.75]
    next_point = [v1.end_point, v2.end_point]
    draw_branches(point=next_point, angle=next_angle, length=next_length, delta=delta)


# draw_branches(point=[point_0, point_0], angle=[90, 105], length=[50, 40], delta=25)


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
# def draw_bunches(start_point=0, angle=90, length=100):
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
#     v1.draw()
#     next_length = length * 0.75
#     next_point = v1.end_point
#     next_angle = angle
#     n=0
#     while n < 2:
#         draw_bunches(start_point=next_point, angle=angle, length=next_length)
#         angle+=10
#         n+=1
# #
#
# # 3) первоначальный вызов:
# root_point = sd.get_point(300, 30)
# for i in range(5, 25, 5):
#     draw_bunches(start_point=root_point, angle=90+i, length=150-i)


# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


root_point = sd.get_point(400, 30)


def draw_bunches(point, angle, length, delta):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    next_point = v1.end_point
    next_angle = random.randint(delta, 180)
    next_length = length * 0.75
    draw_bunches(point=next_point, angle=next_angle, length=next_length, delta=delta)


for i in range(5, 50, 10):
    draw_bunches(point=root_point, angle=120, length=200, delta=i)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
