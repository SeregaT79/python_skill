# -*- coding: utf-8 -*-
import simple_draw as sd

background_color = (255, 255, 255)
# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
point_t = sd.get_point(50, 50)
point_k = sd.get_point(400, 50)
point_p = sd.get_point(400, 400)
point_s = sd.get_point(50, 400)
p_fig = [point_t, point_k, point_p, point_s]

def figure_draw(point=0, delta=0, angle=0, a=50, color=None):
    while angle < 360:
        figure = sd.get_vector(start_point=point, angle=angle, length=a)
        figure.draw(color=color)
        angle += delta
        point = figure.end_point

colors = {
    1: sd.COLOR_RED,
    2: sd.COLOR_ORANGE,
    3: sd.COLOR_YELLOW,
    4: sd.COLOR_GREEN,
    5: sd.COLOR_CYAN,
    6: sd.COLOR_BLUE,
    7: sd.COLOR_PURPLE,
    8: sd.COLOR_DARK_YELLOW,
    9: sd.COLOR_DARK_ORANGE,
    10: sd.COLOR_DARK_RED,
    11: sd.COLOR_DARK_GREEN,
    12: sd.COLOR_DARK_CYAN,
    13: sd.COLOR_DARK_BLUE,
    14: sd.COLOR_DARK_PURPLE,
}
for num, col in colors.items():
    print(num, "-",  col)


color_input = int(input("Введите номер желаемого цвета: "))


for i, j in zip([60, 72, 90, 120], p_fig):
    figure_draw(point=j, delta=i, angle=0, a=50, color=color_input)


sd.pause()
