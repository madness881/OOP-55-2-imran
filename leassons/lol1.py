
class Hero:

    # конструктор класса
    def __init__(self, name="john", lvl=1, hp=10):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # class method методы класса
    def base_action(self):
        if self.lvl == 100:
            return f"{self.name} super Hero"
        return f"{self.name} base Hero"

    def added(self):
        pass



# Объект класса|Экземпляр класса
kirito = Hero(name="Kirito", hp=123)
asuna = Hero("asuna", 100, 1000)
array = [1,2,3]
tuples = (1,2,3)
integer = 123
sting = "123"

print(kirito.lvl)

