
# public
# _protected
# __private

class Passport:
    """
    Создаем класс паспорт
    """
    __pages = 20      # сделали приватным

    def __init__(self, first_name, last_name,date_of_birth, country='Russia'): # функция __init__
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.country = country
        print('Add new passport.')

    def _change_surname(self, new_last_name): # делаем защищенным
        self.last_name = new_last_name

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

    # приватный метод
    def __show_pages(self):
        print(self.__pages)


print(dir(Passport))

