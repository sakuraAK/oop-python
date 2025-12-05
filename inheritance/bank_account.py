"""
Parent: BankAccount

Attributes: owner, balance

Methods: deposit(), withdraw()

Child classes:

SavingsAccount → cannot withdraw more than balance

CheckingAccount → allows overdraft up to –$200

Override withdraw() to reflect rules.

"""
class BankAccount:

    def __init__(self):
        self._balance = 0.0


    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print(f"Insufficient funds")
            return
        self._balance -= amount

    def show_balance(self):
        print(f"Your balance is: {self._balance:,.2f}$")

class SavingAccount(BankAccount):
    pass

class CheckingAccount(BankAccount):
    
    def withdraw(self, amount):
        if self._balance - amount > -200:
            self._balance = self._balance - amount
        else:
            print("Insufficient funds")




saving_account = SavingAccount()
saving_account.deposit(100)
saving_account.show_balance()
saving_account.withdraw(50)
saving_account.show_balance()
saving_account.withdraw(100)
saving_account.show_balance()

checking_account = CheckingAccount()
checking_account.deposit(100)
checking_account.show_balance()
checking_account.withdraw(50)
checking_account.show_balance()
checking_account.withdraw(100)
checking_account.show_balance()