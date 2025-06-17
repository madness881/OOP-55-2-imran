class Product():
    def __init__(self, name, price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_info(self):
        return f'Товар:{self.name},\n Цена:{self.price},\nКол:{self.stock}шт'

    def buy(self,quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            return False

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        if product.buy(quantity):
            self.products.append((product, quantity))
        else:
            print('Недостаточно товара')


    def checkout(self):
        total = 0
        for product, quantity in self.products:
            cost = product.price * quantity
            print(f'{product.name},{quantity}шт. по,{product.price} = {cost}')
            total += cost
        print(f'Итоговая сумма: {total}')

p1 = Product("Клавиатура:RAZER", 50000, 10)
p2 = Product("Мышка:RAZER", 1000, 50)
p3 = Product("Наушники:RAZER", 1500, 100)

cart = Cart()
cart.add_product(p1, 2)
cart.add_product(p2, 5)
cart.add_product(p3, 5)
cart.checkout()
