# -*- coding: utf-8 -*-

import simple_draw as sd

sd.background_color = sd.COLOR_WHITE
sd.resolution = (800, 600)
# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
point = sd.get_point(350, 325)

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

figure_sample = {
    1: 'треугольник',
    2: "квадрат",
    3: 'пятиугольник',
    4: 'шестиугольник'
}

for num, col in colors.items():
    print(num, "-",  col[1])

color_input = int(input("Введите номер желаемого цвета от 0 до 13: "))

print("Какую фигуру будем рисовать?")

for num, fig in figure_sample.items():
    print(num, "-",  fig)

figure_input = int(input('Введите число: '))

if figure_input == 1:
    figure_draw(point=point, delta=120, angle=0, a=100, color=colors[color_input][0])
elif figure_input == 2:
    figure_draw(point=point, delta=90, angle=0, a=100, color=colors[color_input][0])
elif figure_input == 3:
    figure_draw(point=point, delta=72, angle=0, a=100, color=colors[color_input][0])
elif figure_input == 4:
    figure_draw(point=point, delta=60, angle=0, a=100, color=colors[color_input][0])



sd.pause()
