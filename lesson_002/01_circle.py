#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42
pi = 3.1415926

S = round(pi*radius**2, 4)
print(S)

point = (23, 34)
point_2 = (30, 30)

h1 = (point[0]**2 + point[1]**2)**0.5
print(h1 > radius)

h2 = (point_2[0]**2 + point_2[1]**2)**0.5
print(h2 > radius)
