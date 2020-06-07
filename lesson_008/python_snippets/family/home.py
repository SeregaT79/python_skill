from termcolor import cprint

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

    def act(self):
        # Грязь добавляется каждый день по 5 пунктов
        self.dirt += 5
        cprint(f'Грязи прибавилось - {self.dirt},\nеды в доме - {self.food},\nденег - {self.money}')

        if self.dirt > 90:
            self.man.happiness -= 10
            cprint(f'Что-то очень много грязи! Не пора ли убираться?')




