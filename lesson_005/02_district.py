# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import  room1, room2

prob = ', '
print('На районе в первом доме живут:')
print(prob.join(room1.folks))
print(prob.join(room2.folks))
print()

from district.central_street.house2 import room1, room2

print('На районе во втором доме живут:')
print(prob.join(room2.folks))

