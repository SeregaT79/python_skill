from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return f"Я - {self.name}, сытость {self.fullness}, еды осталось {self.food}, денег осталось {self.money}"

    def eat(self):
        if self.food >= 10:
            cprint(f'{self.name} поел', color='yellow')
            self.fullness += 10
            self.food -= 10
        else:
            print(f'{self.name} нет еды')

    def work(self):
        cprint(f'{self.name} сходил на работу', color='red')
        self.money += 50
        self.fullness -= 10

    def play_DOTA(self):
        cprint(f'{self.name} играл в DOTA', color='green')
        self.fullness -= 10

    def shopping(self):
        if self.money >= 50:
            print(f'{self.name} сходил в магазин и купил продуктов')
            self.food += 50
            self.money -= 50
        else:
            print(f'{self.name} деньги кончились')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер', color='cayen')
            return
        
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shopping()
        elif self.money < 50:
            self.work() 
        else:
            self.play_DOTA()        


beavis = Man(name='Бивис')
batthead = Man(name='Батхет')

for day in range(1, 21):
    print(f'\n==================== день {day} ==========================\n')
    vasya.act()
    print(vasya)
