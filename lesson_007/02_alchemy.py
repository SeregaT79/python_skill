# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

class Water:
    _name = "Вода"

    def __add__(self, other):
        if other._name == 'Воздух':
            return Storm._name

        elif other._name == 'Огонь':
            return Steam._name

        elif other._name == 'Земля':
            return Dirt._name

        else:
            return None

    def __str__(self):
        return Water._name


class Air:
    _name = "Воздух"

    def __add__(self, other):
        if other._name == 'Вода':
            return 'Шторм'

        elif other._name == 'Огонь':
            return 'Молния'

        elif other._name == 'Земля':
            return Dust._name
        else:
            return None

    def __str__(self):
        return Air._name


class Fire:
    _name = "Огонь"

    def __add__(self, other):
        if other._name == 'Воздух':
            return Lightning._name

        elif other._name == 'Вода':
            return Steam._name

        elif other._name == 'Земля':
            return Lava._name

        else:
            return None

    def __str__(self):
        return Fire._name


class Earth:
    _name = 'Земля'

    def __add__(self, other):
        if other._name == 'Вода':
            return Dirt._name

        elif other._name == 'Воздух':
            return Dust._name

        elif other._name == 'Огонь':
            return Lava._name

        else:
            return None

    def __str__(self):
        return Earth._name


class Storm:
    _name = 'Шторм'

    def __str__(self):
        return Storm._name


class Steam:
    _name = 'Пар'

    def __str__(self):
        return Steam._name

class Dirt:
    _name = 'Грязь'

    def __str__(self):
        return Dirt._name


class Lightning:
    _name = 'Молния'

    def __str__(self):
        return Lightning._name


class Dust:
    _name = 'Пар'

    def __str__(self):
        return Dust._name


class Lava:
    _name = 'Лава'

    def __str__(self):
        return Lava._name


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.