#Наследование
#Полиморфизм

#Родительский класс
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print (f"{self.name} action!!!")
#Дочерний класс///Класс наследник

class WarriorHero(Hero):

    def action(self):
        print (f"WarriorHero method")
    def __init__(self,name,lvl,hp,st):
        super().__init__(name,lvl,hp)
        self.st = st

hero_1 = WarriorHero("Hero 1", 10, 1000,102)

hero_1.action()




