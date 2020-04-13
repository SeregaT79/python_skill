# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

x1 = sd.get_point(50, 50)
x2 = sd.get_point(350, 450)

sd.line(sd.get_point(50, 50), sd.get_point(350, 450), color=rainbow_colors[0], width=5)
sd.line(sd.get_point(55, 50), sd.get_point(355, 450), color=rainbow_colors[1], width=5)
sd.line(sd.get_point(60, 50), sd.get_point(360, 450), color=rainbow_colors[2], width=5)
sd.line(sd.get_point(65, 50), sd.get_point(365, 450), color=rainbow_colors[3], width=5)
sd.line(sd.get_point(70, 50), sd.get_point(370, 450), color=rainbow_colors[4], width=5)
sd.line(sd.get_point(75, 50), sd.get_point(375, 450), color=rainbow_colors[5], width=5)
sd.line(sd.get_point(80, 50), sd.get_point(380, 450), color=rainbow_colors[6], width=5)



# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

x = sd.get_point(400, -450)

r = 650
sd.circle(x, radius=r, color=rainbow_colors[0], width=50)
r+=50
sd.circle(x, radius=r, color=rainbow_colors[1], width=50)
r+=50
sd.circle(x, radius=r, color=rainbow_colors[2], width=50)
r+=50
sd.circle(x, radius=r, color=rainbow_colors[3], width=50)
r+=50
sd.circle(x, radius=r, color=rainbow_colors[4], width=50)
r+=50
sd.circle(x, radius=r, color=rainbow_colors[5], width=50)
r+=50
sd.circle(x, radius=r, color=rainbow_colors[6], width=50)


sd.pause()
