import simple_draw as sd
import random
sd.background_color = (255, 255, 255)

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

point_t = sd.get_point(50, 50)
point_k = sd.get_point(400, 50)
point_p = sd.get_point(400, 400)
point_s = sd.get_point(50, 400)
p_fig = [point_t, point_k, point_p, point_s]

def figure_draw(point=0, delta=0, angle=0, a=50, color=0):
    """
    Рисуем фигуры
    :param point: начальная точка
    :param delta: величина изменения угла
    :param angle: угол
    :param a: сторона фигуры
    :param color: цвет
    :return: возвращает треугольник
    """
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


def col_imp(point):
    for num, col in colors.items():
        print(num, "-", col[1])

    figure_sample = {
        1: 'треугольник',
        2: "квадрат",
        3: 'пятиугольник',
        4: 'шестиугольник'
    }

    color_input = int(input("Введите номер желаемого цвета от 0 до 13: "))

    print("Какую фигуру будем рисовать?")

    for num, col in figure_sample.items():
        print(num, "-", col[1])

    figure_input = int(input('Введите число: '))

    if figure_input == 1:
        figure_draw(point=point, delta=120, angle=0, a=100, color=colors[color_input][0])
    elif figure_input == 2:
        figure_draw(point=point, delta=90, angle=0, a=100, color=colors[color_input][0])
    elif figure_input == 3:
        figure_draw(point=point, delta=72, angle=0, a=100, color=colors[color_input][0])
    elif figure_input == 4:
        figure_draw(point=point, delta=60, angle=0, a=100, color=colors[color_input][0])

    return


def draw_bunches(point, angle, length, delta):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    next_point = v1.end_point
    next_angle = random.randint(delta, 180)
    next_length = length * 0.75
    draw_bunches(point=next_point, angle=next_angle, length=next_length, delta=delta)


def snow(y, delta=random.uniform(1, 2)):

    x = random.randint(15, 300)
    x1 = random.randint(50, 400)
    x2 = random.randint(100, 500)
    x3 = random.randint(150, 600)
    x4 = random.randint(50, 700)
    x5 = random.randint(20, 700)
    x6 = random.randint(125, 700)
    x7 = random.randint(140, 700)
    x8 = random.randint(200, 700)
    x9 = random.randint(231, 700)

    length = random.randint(10, 50)
    length_1 = random.randint(10, 50)
    length_2 = random.randint(10, 50)
    length_3 = random.randint(10, 50)
    length_4 = random.randint(10, 50)
    length_5 = random.randint(10, 50)
    length_6 = random.randint(10, 50)
    length_7 = random.randint(10, 50)
    length_8 = random.randint(10, 50)
    length_9 = random.randint(10, 50)

    while True:
        sd.start_drawing()

        point_0 = sd.get_point(x, y)
        sd.snowflake(center=point_0, length=length)

        point_1 = sd.get_point(x1, y)
        sd.snowflake(center=point_1, length=length_1)

        point_2 = sd.get_point(x2, y)
        sd.snowflake(center=point_2, length=length_2)

        point_3 = sd.get_point(x3, y)
        sd.snowflake(center=point_3, length=length_3)

        point_4 = sd.get_point(x4, y)
        sd.snowflake(center=point_4, length=length_4)

        point_5 = sd.get_point(x5, y)
        sd.snowflake(center=point_5, length=length_5)

        point_6 = sd.get_point(x6, y)
        sd.snowflake(center=point_6, length=length_6)

        point_7 = sd.get_point(x7, y)
        sd.snowflake(center=point_7, length=length_7)

        point_8 = sd.get_point(x8, y)
        sd.snowflake(center=point_8, length=length_8)

        point_9 = sd.get_point(x9, y)
        sd.snowflake(center=point_9, length=length_9)



        y -= 20
        if y < 50:
            break

        sd.finish_drawing()
        sd.sleep(0.1)

        sd.snowflake(center=point_0, length=length, color=sd.background_color)
        x = x * 1.02 + random.uniform(-10.1, 10.1)


        sd.snowflake(center=point_1, length=length_1, color=sd.background_color)
        x1 = x1 * 1.02 + random.uniform(-10.1, 10.1)


        sd.snowflake(center=point_2, length=length_2, color=sd.background_color)
        x2 = x2 * 1.02 + random.uniform(-10.1, 10.1)


        sd.snowflake(center=point_3, length=length_3, color=sd.background_color)
        x3 = x3 * 1.02 + random.uniform(-10.1, 10.1)


        sd.snowflake(center=point_4, length=length_4, color=sd.background_color)
        x4 = x4 * 1.02 + random.uniform(-10.1, 10.1)


        sd.snowflake(center=point_5, length=length_5, color=sd.background_color)
        x5 = x5 * 1.01 + random.uniform(-10.1, 10.1)


        sd.snowflake(center=point_6, length=length_6, color=sd.background_color)
        x6 = x6 * 1.011 + random.uniform(-10.1, 10.1)


        sd.snowflake(center=point_7, length=length_7, color=sd.background_color)
        x7 = x7 * 1.001 + random.uniform(-10.1, 10.1)


        sd.snowflake(center=point_8, length=length_8, color=sd.background_color)
        x8 = x8 * 1.0001 + random.uniform(-10.1, 10.1)

        sd.snowflake(center=point_9, length=length_9, color=sd.background_color)
        x9 = x9 * 1.000001 + random.uniform(-10.1, 10.1)



















