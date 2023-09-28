
class Client():
    # создаем покупателя интернет-магазина
    def __init__(self, email, order_num, registration_year, discount=0):
        self.email = email
        self.order_num = order_num
        self.registration_year = registration_year
        self.discount = discount

    # оформление заказа
    def make_order(self, price):
        self.update_discount()
        self.order_num += 1
        discounted_price = price * (1 - self.discount)
        print(f'Price for {self.email} is {discounted_price} dollars')

    # формирование скидки
    def update_discount(self):
        if self.registration_year < 2020 and self.order_num >= 5:
            self.discount = 0.1

# создаем покупателей
clients_db = [
    Client('anna@mail.ru', 2, 2023),
    Client('kwenus@gmail.com', 10, 2015),
    Client('mons@rambler.ru', 4, 2017)
]

# делаем покупки
clients_db[0].make_order(100)
clients_db[1].make_order(200)
clients_db[2].make_order(500)
clients_db[2].make_order(400)

