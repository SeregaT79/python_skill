from home import House
from termcolor import cprint
from random import randint


# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.

# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

class Man:
    def __init__(self, name):
        # У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
        self.house = None
        self.name = name
        self.fullness = 30
        self.happiness = 100

    def eat(self):
        self.fullness += 30
        self.house.food -= 30
        self.happiness += 3
        cprint(f"{self.name} покушал, сытость {self.fullness}, счастья {self.happiness}", color='green')

    def my_home(self, house):
        self.house = house
        cprint(f'{self.name} живет в красивом доме', color='yellow')

    def __str__(self):
        return f"А вот и я!"


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        phrase = super().__str__()
        return phrase + f" Меня зовут {self.name}"

    def work(self):
        #   ходить на работу,
        # Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
        self.house.money += 350
        cprint(f'{self.name} сходил на работу', color='blue')

    def gaming(self):
        #   играть в WoT,
        # Степень счастья растет: у мужа от игры в WoT (на 20),
        self.happiness += 20
        self.fullness -= 5
        cprint(f'{self.name} поиграл в WoT', color='cyan')

    def pick_up_cat(self, house):
        cprint(f'{self.name} подобрал кота', color='yellow')
        self.house = house
        self.house.cat_food += 20

    def act(self):
        if self.house.money < 250:
            self.work()

        if self.fullness < 15:
            self.eat()

        # Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
        if self.fullness <= 0:
            cprint(f'{self.name} умер', color='red')

        dice = randint(1, 3)
        if dice != 1:
            self.gaming()

        if self.house.dirt > 90:
            self.happiness -= 10
            cprint(f'Что-то очень много грязи! Не пора ли убираться?', color='grey')


class Wife(Man):
    coat = 0

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        phrase = super().__str__()
        return phrase + f" Меня зовут {self.name}"

    def shopping(self):
        #   покупать продукты,
        # Еда стоит 10 денег 10 единиц еды.
        if self.house.cat_food < 10:
            self.house.cat_food += 20
            self.house.money -= 100
            self.house.food += 100
            self.fullness -= 5
            cprint(f'{self.name} купила продуктов и коту еды', color='white')
        else:
            self.house.money -= 100
            self.house.food += 100
            self.fullness -= 5
            cprint(f'{self.name} купила продуктов', color='white')

    def buy_fur_coat(self):
        # у жены степень счастья растет от покупки шубы (на 60, но шуба дорогая)
        #   покупать шубу, Шуба стоит 350 единиц.
        self.happiness += 60
        self.house.money -= 150
        cprint(f'{self.name} купила шубу', color='cyan')

    def clean_house(self):
        #   убираться в доме,
        #   за одну уборку жена может убирать до 100 единиц грязи.
        self.house.dirt -= 100
        self.happiness += 2
        self.fullness -= 5
        cprint(f'{self.name} убралась в доме', color='yellow')

    def go_beauty_saloon(self):
        self.house.money -= 60
        self.happiness += 15
        self.fullness -= 15
        cprint(f'{self.name} сходила в салон красоты', color='magenta')

    def act(self):

        if self.fullness < 15:
            self.eat()
        # Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,

        if self.fullness <= 0:
            cprint(f'{self.name} умерла', color='red')

        if self.house.dirt > 100:
            self.clean_house()

        if self.house.food < 60:
            self.shopping()

        if self.house.cat_food < 12:
            self.shopping()

        dice = randint(1, 6)
        if dice == 2:
            self.go_beauty_saloon()
        elif dice == 5 and self.house.money > 550:
            self.buy_fur_coat()
            self.coat += 1

        if self.house.dirt > 90:
            self.happiness -= 10
            cprint(f'Что-то очень много грязи! Не пора ли убираться?')


class Child(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        res = super().__str__()
        cprint(res + f"{self.name} теперь с нами", color='magenta')

    def act(self):
        self.eat()

    def eat(self):
        self.house.food -= 10

    def sleep(self):
        pass
