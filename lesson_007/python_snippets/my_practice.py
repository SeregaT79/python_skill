class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return f"Я - {self.name}, сытость {self.fullness}, еды осталось {self.food}, денег осталось {self.money}"

    def eat(self):
        if self.food > 10:
            print(f'{self.name} поел')
            self.fullness += 10 
            self.food -= 10
        else:
            print(f'{self.name} нет еды')

    def work(self):
        print(f'{self.name} сходил на работу')
        self.money += 50
        self.fullness -= 10

    def play_DOTA(self):
        print(f'{self.name} играл в DOTA')
        self.fullness -= 10


man = Man(name='Вася')
print(man)
man.eat()
print(man)
man.work()
