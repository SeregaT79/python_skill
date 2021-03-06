# -*- coding: utf-8 -*-
import random
import simple_draw as sd
from snowfall import snowflake, snowflaks_go

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)


while True:
    x, y = random.randint(10, 600), random.randint(500, 550)
    sd.start_drawing()
    snowflake(N=5, x=x, y=y, color=sd.background_color)#  нарисовать_снежинки_цветом(color=sd.background_color)
    x, y = snowflaks_go(x0=x, y0=y) #  сдвинуть_снежинки()
    snowflake(N=5, x=x, y=y, color=sd.COLOR_CYAN) #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
