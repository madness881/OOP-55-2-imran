# # class Hero:
# #     def __init__(self,hp,lvl):
# #         self.hp = hp
# #         self.lvl = lvl
# #
# #
# #     # def __str__(self):
# #     #     return f"Как дела герой?"
# #
# #     def __add__(self,other):
# #         return Hero(self.hp+other.hp,self.lvl+other.lvl)
# #
# #     def __gt__(self,other):
# #         if self.hp > other.hp:
# #             return 'Правильно'
# #         else:
# #             return 'Не правильно'
# #
# # v1 = Hero(10,1)
# # v2 = Hero(10,2)
# # v3 = v1 < v2
# #
# # print(f'{v3}')
# #
# 🧪 Уровень 1 — Базовые магические методы
# ✅ Задача 1: __str__ и __repr__
# Создай класс Weapon, у которого есть name и damage. Переопредели:
#
# __str__ — чтобы печатался красивый вид, например:
# "Меч ниндзя: 100 урона"
#
# __repr__ — чтобы для отладки выводилось:
# Weapon(name='Нож', damage=50)


class Weapon:
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"Оружие:{self.name}, урон составляет {self.damage}"

    def __repr__(self):
        return f"Weapon: {self.name},damage: {self.damage}"

    def __add__(self,other):
        new_name = f"Комбо: {self.name} + {other.name}"
        new_damage = self.damage + other.damage
        return  Weapon(new_name,new_damage)
    def __gt__(self,other):
        return self.damage > other.damage
    def __eq__(self,other):
        return self.damage == other.damage and self.name == other.name
    def __bool__(self):
        return self.damage > 0
    def status(self):
        return "Оружие может наносить урон" if self.damage >0 else "Чувак,У ТЕБЯ ПАЛКА"

w1 = Weapon("Кинжал",50)
w2 = Weapon("Катана ТЕРМИНАТОРА",0)

w3 = w1 + w2





print(w3)
print(w2.status())
print(w1.status())
print(w2.__str__())