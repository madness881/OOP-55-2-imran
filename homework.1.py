

class Person:
    def __init__(self, name, age,city):
        self.name = name
        self.age = age
        self.city = city
    def introduce(self):
        print(f'Привет меня зовут {self.name}, мне {self.age}, и мой город {self.city}')

    def is_adult(self):
        if self.age >= 18:
            return  True
        else:
            return False
Imran = Person('Imran', 19, 'Bishkek')
Subaru = Person('Subaru', 17, 'Tokyo')
Johan_Libert = Person('Johan Libert', 18, 'Haina')

Imran.introduce()
print(Imran.is_adult())
Subaru.introduce()
print(Subaru.is_adult())
Johan_Libert.introduce()
print(Johan_Libert.is_adult())