from termcolor import cprint
from random import randint


class House:
    # Все они живут в одном доме, дом характеризуется:
    #   кол-во денег в тумбочке (в начале - 100)
    #   кол-во еды в холодильнике (в начале - 50)
    #   кол-во грязи (в начале - 0)

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.man = None
        self.cat_food = 30

    def act(self):
        # Грязь добавляется каждый день по 5 пунктов
        self.dirt += 5
        cprint(f"Грязи прибавилось - {self.dirt},\nеды в доме - {self.food},\nденег - {self.money}, еды для кота "
               f"осталось - {self.cat_food}")


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
        self.house.dirt += 5
        self.fullness_cat -= 10
        cprint(f"Кот {self.name} весь день драл обои")

    def my_home(self, house):
        self.house = house
        self.fullness_cat += 10
        cprint(f"Кот {self.name} поселился в доме")

    def act(self):
        if self.fullness_cat <= 0:
            cprint(f'Кот {self.name} умер', color='cyan')
            return

        if self.fullness_cat < 20:
            self.cat_eats()

        dice = randint(1, 5)
        if dice == 2 or dice == 4:
            self.cat_sleep()
        elif dice == 1 or dice == 3:
            self.tear_wallpaper()
