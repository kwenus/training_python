from OOP_3 import User

class Friend(User):
    def __init__(self, name, phone, addres):
        # наследуем всю логику из родительского класса
        super().__init__(name, phone)
        # добавляем новую функциональность
        self.addres = addres

    # переопределение методов
    def show(self):
        print(f'{self.name}, contact phone number: ({self.phone}), addres: {self.addres}')

user_3 = Friend('Anna', '+799999', 'Kazan')

user_3.show()

#print(Friend.mro())