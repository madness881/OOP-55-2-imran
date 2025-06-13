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
    def __init__(self,name,hp,damage,arrows=5,precision=80):
        super().__init__(name,hp,damage)
        self.arrows = arrows
        self.precision = precision


Assain = Archer("Assain",10,100,15,99)
Assain.action()
Assain.attack()
