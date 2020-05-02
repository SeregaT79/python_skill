# -*- coding: utf-8 -*-
import simple_draw as sd
import random


def snowflake(N, x, y, color=sd.COLOR_WHITE):

    """
    :param N: число снежинок
    :return: указанное число снежинок
    """

    for i in range(N):
        point = sd.get_point(x, y)
        sd.snowflake(point, length=random.randint(10, 50), color=color)
        sd.sleep(0.1)


def snowflaks_go(x0, y0, delta_x=20, delta_y=20):
    x = x0 + delta_x
    y = y0 - delta_y
    return x, y


