# Bank accout
# Does not allow overdraft


class BankAccount:
    bank_code = "RBC"
    account_counter = 0

    def __init__(self, owner):
        BankAccount.account_counter += 1
        self.__account_number = f"{BankAccount.bank_code}-{BankAccount.account_counter}"
        self.__owner = owner
        self.__balance = 0


    def get_balance(self):
        print(f"""Account number: {self.__account_number} 
              Owner: {self.__owner}
              Balance: {self.__balance}""")


    def deposit(self, amount):
        if amount < 0:
            raise ValueError(f"Deposit amount cannot be negative")

        self.__balance += amount
    
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError(f"Not enough funds")
        self.__balance -= amount


acc1 = BankAccount('Andrey K')
acc2 = BankAccount('John Doe')
acc1.deposit(300)
acc2.deposit(500)

acc1.withdraw(50)
acc2.withdraw(100)

acc1.get_balance()
acc2.get_balance()










