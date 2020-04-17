# -*- coding: utf-8 -*-
import simple_draw as sd

sd.background_color = (255, 255, 255)
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

def figure_draw(point=0, delta=0, angle=0, a=50, color=0):
    while angle < 360:
        figure = sd.get_vector(start_point=point, angle=angle, length=a, width=2)
        figure.draw(color=color)
        angle += delta
        point = figure.end_point

colors = {
    0: [sd.COLOR_RED,'red'],
    1: [sd.COLOR_ORANGE, 'orange'],
    2: [sd.COLOR_YELLOW, 'yellow'],
    3: [sd.COLOR_GREEN, 'green'],
    4: [sd.COLOR_CYAN, 'cyan'],
    5: [sd.COLOR_BLUE, 'blue'],
    6: [sd.COLOR_PURPLE,'purple'],
    7: [sd.COLOR_DARK_YELLOW, 'dark_yellow'],
    8: [sd.COLOR_DARK_ORANGE, 'dark_orange'],
    9: [sd.COLOR_DARK_RED, 'dark_red'],
    10: [sd.COLOR_DARK_GREEN, 'dark_green'],
    11: [sd.COLOR_DARK_CYAN, 'dark_cyan'],
    12: [sd.COLOR_DARK_BLUE, 'dark_blue'],
    13: [sd.COLOR_DARK_PURPLE, 'dark_purple']
}
for num, col in colors.items():
    print(num, "-",  col[1])


color_input = int(input("Введите номер желаемого цвета от 0 до 13: "))


for i, j in zip([60, 72, 90, 120], p_fig):
    figure_draw(point=j, delta=i, angle=0, a=50, color=colors[color_input][0])


sd.pause()
