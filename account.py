from random import randint

class Account:
    def __init__(self, name, email, address, account_type) -> None:
        self.__balance = 0
        self.__account_no = str(randint(1e9, 2e9))
        self.__transactions = []
        self.__loans = []
        self.__name = name
        self.__email = email
        self.__address = address
        self.__account_type = account_type
    
    @property
    def account_no(self):
        return self.__account_no

    @property
    def balance(self):
        return self.__balance
    
    @property
    def transactions(self):
        return self.__transactions
    
    @staticmethod
    def check_valid_amount(amount):
        if not amount>0:
            raise Exception(f"Invalid Amount")

    def deposit(self, amount):
        Account.check_valid_amount(amount)
        self.__balance += amount
        self.__transactions.append(amount)

    def withdraw(self, amount):
        Account.check_valid_amount(amount)
        if self.__balance < amount:
            raise Exception("Withdrawal amount exceeded")
        self.__balance -= amount
        self.__transactions.append(-amount)

    def take_loan(self, amount):
        Account.check_valid_amount(amount)
        if len(self.__loans) < 2: 
           self.__loans.append(amount)
           self.__balance += amount
           self.__transactions.append(amount)
        else:
            raise Exception(f"Maximum loans are already taken")
        
    def __repr__(self) -> str:
        return f"account no: '{self.account_no}' | name: '{self.__name}' | email: '{self.__email}' | address: '{self.__address}' | account type: '{self.__account_type}'"