# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (1100, 600)
ix = 0
jy = 0

left_bottom = sd.get_point(0, 0)
right_top = sd.get_point(100, 50)


for i in range(0, 700, 50):
    for k in range(0, 1300, 100 ):
        sd.rectangle(sd.get_point(ix, jy), sd.get_point(ix+k, jy+i), width=2)


sd.pause()