from home import House
from termcolor import cprint


#
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

    def sleeping(self):
        self.fullness -= 10
        self.happiness += 3
        cprint(f"{self.name} отдохнул, счастья {self.happiness}", color='green')

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
        self.house.money += 150
        return f'{self.name} сходил на работу'

    def gaming(self):
        #   играть в WoT,
        # Степень счастья растет: у мужа от игры в WoT (на 20),
        self.happiness += 20
        self.fullness -= 5
        return f'{self.name} поиграл в WoT'

    def act(self):
        # Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
        if self.fullness <= 0:
            cprint(f'{self.name} умер', color='red')



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
        self.house.money -= 100
        self.house.food += 100
        self.fullness -= 5
        return f'{self.name} купила продуктов'

    def buy_fur_coat(self):
        # у жены степень счастья растет от покупки шубы (на 60, но шуба дорогая)
        #   покупать шубу, Шуба стоит 350 единиц.
        self.happiness += 60
        self.house.money -= 350
        coat += 1
        return f'{self.name} купила шубу'

    def clean_house(self):
        #   убираться в доме,
        #   за одну уборку жена может убирать до 100 единиц грязи.
        self.house.dirt -= 100
        self.happiness += 2
        self.fullness -= 5
        return f'{self.name} убралась в доме'

    def act(self):
        # Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,

        if self.fullness <= 0:
            cprint(f'{self.name} умерла', color='red')

        if self.house.dirt > 150:
            self.clean_house()

        if 0 < self.house.food < 60:
            self.shopping()

        if self.house.money > 400:
            self.buy_fur_coat()


husband = Husband(name='Серега')
wife = Wife(name="Аня")
home = House()
in_home = [husband, wife]

if __name__ == '__main__':
    day = 1

    for man in in_home:
        man.my_home(home)

    while day < 15:
        print('*' * 10, f'{day}', '*' * 10)
        husband.act()
        wife.act()
        home.act()
        day += 1
