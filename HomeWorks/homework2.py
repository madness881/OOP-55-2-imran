class Heroes:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def action(self):
        print(f'{self.name} Копим ульту...!')
    def attack(self):
        print(f'{self.name} СЕЙЧАС БУДЕТ АТАКОВАТЬ!')
        print(f"Хп персонажа на данный момент: {self.hp}")
        print(f"Персонаж нанес урон: {self.damage}")
class Archer(Heroes):
    def __init__(self,name,hp,damage,arrows=5,precision=50):
        super().__init__(name,hp,damage)
        self.arrows = arrows
        self.precision = precision
    def attack(self):
        self.arrows -= 1
        print(f'Количество стрел уменьшилось: {self.arrows}')

        if self.precision >= 70:
            print('Атака удачна')
        else:
            print('Атака неудачна')
    def rest(self):
        print(f"Если у вас останется меньше 5 стрел, мы пополним их на 5")
        if self.arrows <= 5:
            self.arrows += 5
            print(f'Стрелы пополнились: {self.arrows}')

    def status(self):
        print(f'СТАТИСТИКА:\n |Имя:{self.name}\n |ХП:{self.hp}\n |Урон:{self.damage}\n |Точность:{self.precision}')



Assain = Archer("Assain",10,100,4,69)
Assain.action()
Assain.attack()
Assain.rest()
Assain.status()

