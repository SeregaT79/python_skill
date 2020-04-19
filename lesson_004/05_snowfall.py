# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
point_0 = sd.get_point(100, 500)
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


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





for i in range(20):
    snow(550)


sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


