
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Not enough money')
            return
        self.balance -= amount


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        if isinstance(account, Account):   # проверяем относится ли объект к необходимому классу
            self.accounts.append(account)
        else:
            print("Error")

    def remove_account(self, account):
        self.accounts.remove(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return 'Account not found'

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        account.withdraw(amount)



account_1 = Account(33)
account_2 = Account(34, 100)

# print(account_1.balance)
# account_1.deposit(200)
# print(account_1.balance)
#
# account_2.withdraw(130)

mega_bank = Bank()
mega_bank.add_account(account_1)
mega_bank.add_account(account_2)

mega_bank.deposit(33, 1000)
mega_bank.deposit(34, 2000)

mega_bank.withdraw(33, 128)
mega_bank.withdraw(34, 220)

for account in mega_bank.accounts:
    print(account.balance)
