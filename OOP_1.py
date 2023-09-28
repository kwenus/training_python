

# пишем атрибуты класса
class Passport:
    """
    Создаем класс паспорт
    """
    pages = 20      # так делают атрибуты класса

    def __init__(self, first_name, last_name,date_of_birth, country='Russia'): # функция __init__
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.country = country
        print('Add new passport.')

    def change_surname(self, new_surname):
        self.surname = new_surname

    def add_visa(self, visa_name):
        if not hasattr(self, 'visas'):  # функция которая проверяет наличие атрибута
            self.visas = visa_name
        else:
            self.visas.append(visa_name)

    def print_all_visas(self):
        if not hasattr(self, 'visas'):
            print('No visas')
        else:
            print(f"Список всех виз: {', '.join(self.visas)}")

    def show_info(self):
        print(f'Name: {self.first_name}, Surname: {self.last_name}, Date of birth: {self.date_of_birth}, Contry: {self.country}')



passport_1 = Passport('Kostya', 'Kanatev', '10/10/1982')
passport_1.show_info()

# passport_2 = Passport()
#
# # print(passport_1.pages)
#
# passport_2.name = 'Kostya'  # так создаются атрибуты экземпляра класса (сразу в экземпляре)
# passport_1.name = 'Anna'
# passport_1.pages = 21  # так тоже можно, но обычно так не делают
#
# # docs = [passport_1, passport_2]
# # for doc in docs:
# #     print(f'{doc.name} has {doc.pages} pages in passport')
#
# passport_1.visas = ['visa_1', 'visa_2']
# passport_1.print_all_visas()
# passport_1.add_visa('visa_3')
# passport_1.print_all_visas()
#
# passport_2.print_all_visas()
#
#
