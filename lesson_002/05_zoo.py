#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

zoo[1] = "bear"
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
zoo.append(birds[0])
zoo.append(birds[1])
zoo.append(birds[2])
print(zoo)

del zoo[2]
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
print(f"Лев сидит в {zoo.index('lion')+1} клетке")
print(f"Лев сидит в {zoo.index('lark')+1} клетке")


