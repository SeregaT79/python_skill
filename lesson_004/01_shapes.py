# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 600)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
#
# def treangle(point=0, angle=0, a=50):
#     while angle < 360:
#         figure = sd.get_vector(start_point=point, angle=angle, length=a)
#         figure.draw()
#         angle += 120
#         point = figure.end_point
#
#
# def kwadrat(point=0, angle=0, a=50):
#     while angle < 360:
#         figure = sd.get_vector(start_point=point, angle=angle, length=a)
#         figure.draw()
#         angle += 90
#         point = figure.end_point
#
# def pyatiangle(point=0, angle=0, a=50):
#     while angle < 360:
#         figure = sd.get_vector(start_point=point, angle=angle, length=a)
#         figure.draw()
#         angle += 72
#         point = figure.end_point
#
#
# def shestiangle(point=0, angle=0, a=50):
#     while angle < 360:
#         figure = sd.get_vector(start_point=point, angle=angle, length=a)
#         figure.draw()
#         angle += 60
#         point = figure.end_point

# point_t = sd.get_point(50, 50)
# point_k = sd.get_point(400, 50)
point_p = sd.get_point(400, 400)
# point_s = sd.get_point(50, 400)
#
# kwadrat(point=point_k, a=100)
# treangle(point=point_t, a=150)
# pyatiangle(point=point_p, a=100)
# shestiangle(point=point_s, a=100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def figure_draw(point=0, delta=0, angle=0, a=50):
    while angle < 360:
        figure = sd.get_vector(start_point=point, angle=angle, length=a)
        figure.draw()
        angle += delta
        point = figure.end_point



figure_draw(point=point_p, angle=30, a=45, delta=90)


sd.pause()
