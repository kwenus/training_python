
class Passport:
    pages = 20

    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def change_surname(self, new_surname):
        self.surname = new_surname

    def add_visa(self, visa_name):
        if not hasattr(self, 'visas'):
            self.visas = [visa_name]
        else:
            self.visas.append(visa_name)

    def print_all_visas(self):
        if not hasattr(self, 'visas'):
            print('No visas')
        else:
            print(f"Список всех виз: {', '.join(self.visas)}")

    def show_info(self):
        print(f'Name: {self.first_name}, Surname: {self.last_name}, Date of birth: {self.date_of_birth}')

class Foreign_Passport(Passport):
    def __init__(self, first_name, last_name, date_of_birth, country):
        super().__init__(first_name, last_name, date_of_birth)
        self.country = country

    def show_info(self):
        print(f'Name: {self.first_name}, Surname: {self.last_name}, Date of birth: {self.date_of_birth}, Country: {self.country}')

foreign_1 = Foreign_Passport('Karl', 'Capet', '1712', 'France')
foreign_1.show_info()
