# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from termcolor import cprint
import random


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return f"Я - {self.name}, сытость {self.fullness}"

    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} поел', color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            print(f'{self.name} нет еды')

    def work(self):
        cprint(f'{self.name} сходил на работу', color='red')
        self.house.money += 150
        self.fullness -= 5

    def watch_MTV(self):
        self.fullness -= 5
        cprint(f'{self.name} целый день смотрел MTV', color='green')

    def shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} сходил в магазин и купил продуктов', color='magenta')
            self.house.food += 50
            self.house.money -= 50
        else:
            print(f'{self.name} деньги кончились')

    def go_in_to_house(self, house):
        self.house = house
        self.fullness -= 5
        cprint(f'{self.name} поселился в доме ', color='cyan')

    def pick_up_cat(self, house):
        cprint(f'{self.name} подобрал кота', color='yellow')
        self.house = house
        self.house.cat_food += 20

    def buy_cat_food(self):
        if self.house.cat_food < 20:
            cprint(f'{self.name} сходил в магазин и купил коту еды', color='magenta')
            self.house.cat_food += 150
            self.house.money -= 60
        else:
            print(f'{self.name} деньги кончились')

    def clean_mud(self):
        cprint(f'{self.name} убрался в доме', color='magenta')
        self.house.mud -= 100
        self.fullness -= 20

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер', color='cyan')
            return

        if self.house.money < 50:
            self.work()
            return

        if self.house.cat_food <= 5:
            self.buy_cat_food()
            return

        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cat_food < 10:
            self.buy_cat_food()
        elif self.house.mud >= 100:
            self.clean_mud()
        else:
            self.watch_MTV()


class House:
    def __init__(self):
        self.food = 10
        self.money = 50
        self.cat_food = 0
        self.mud = 0

    def __str__(self):
        return f"Еды в доме осталось {self.food}, денег осталось {self.money}\nЕды для кота осталось {self.cat_food}, а грязи вдоме {self.mud}"


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness_cat = 30
        self.house = None

    def __str__(self):
        return f'Я кот {self.name}, моя сытость {self.fullness_cat}'

    def cat_eats(self):
        if self.house.cat_food >= 5:
            cprint(f'Кот {self.name} поел', color='yellow')
            self.fullness_cat += 10
            self.house.cat_food -= 10
        else:
            print(f'{self.name} нет еды')

    def cat_sleep(self):
        self.fullness_cat -= 10
        cprint(f"Кот {self.name} поспал")

    def tear_wallpaper(self):
        self.house.mud += 5
        self.fullness_cat -= 10
        cprint(f"Кот {self.name} весь день драл обои")

    def go_in_to_house(self, house):
        self.house = house
        self.fullness_cat += 10
        cprint(f"Кот {self.name} поселился в доме")

    def act(self):
        if self.fullness_cat <= 0:
            cprint(f'Кот {self.name} умер', color='cyan')
            return


        if self.fullness_cat < 20:
            self.cat_eats()
            self.cat_sleep()
        else:
            self.tear_wallpaper()


citizens = [
    Man(name='Бивис'),
    Man(name='Батхет'),
    Cat(name='Tom'),
    Cat(name='Dus'),
    Cat(name='Straus')
]

my_sweet_house = House()

for citizen in citizens:
    citizen.go_in_to_house(house=my_sweet_house)
Man(name='Бивис').pick_up_cat(my_sweet_house)
Man(name='Батхет').pick_up_cat(my_sweet_house)
Man(name='Батхет').pick_up_cat(my_sweet_house)

for day in range(1, 367):
    print(f'\n==================== день {day} начало ======================')
    for citizen in citizens:
        citizen.act()
    print(f'==================== в конце дня =========================')
    for citizen in citizens:
        citizen.act()
    print(my_sweet_house)


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
