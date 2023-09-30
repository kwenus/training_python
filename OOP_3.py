
class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f'{self.name}, my phone: ({self.phone})')

# дочерний класс
class Friend(User):
    pass

user_1 = User('Kostya', '+79000000')
user_2 = Friend('Anya', "+7900002")

user_1.show()
user_2.show()

