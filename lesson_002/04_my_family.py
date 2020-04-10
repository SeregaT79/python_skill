#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:
from  pprint import pprint
# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['мама', "папа", "брат", "сестра"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    [my_family[0], 162],
    [my_family[1], 167],
    [my_family[2], 178],
    [my_family[3], 143]
]

# pprint((my_family_height))
# Выведите на консоль рост отца в формате
print(my_family_height[1][0], '-', my_family_height[1][1])

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
print(my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1])
