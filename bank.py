from account import Account
from admin import Admin

class Bank:
    def __init__(self) -> None:
        self.__accounts = []
        self.__loans = []
        self.__balance = 0
        self.__admin = None
        self.__is_bankrupt = False
        self.__loan_active = True

    @property
    def is_loan_active(self):
        return self.__loan_active

    @property
    def admin(self):
        return self.__admin

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.__accounts.append(account)
        return account

    def create_admin(self, name, password):
        if self.__admin is None:
            self.__admin = Admin(name, password)
            return self.__admin
        else: 
            raise Exception(f"Admin already exists.")
        
    def get_account(self, account_no):
        account = None
        for ac in self.__accounts:
            if ac.account_no == account_no:
                account = ac
                break
        if account is None:
            raise Exception(f"Account does not exist")
        return account

    def deposit(self, account_no, amount):
        account = self.get_account(account_no)
        account.deposit(amount)
        self.__balance += amount

    def withdraw(self, account_no, amount):
        if self.__is_bankrupt:
            raise Exception(f"The bank is bankrupt")
        account = self.get_account(account_no)
        account.withdraw(amount)
        self.__balance -= amount

    def take_loan(self, account_no, amount):
        if not self.__loan_active:
            raise Exception(f"Loan is currently disabled")
        account = self.get_account(account_no)
        account.take_loan(amount)
        self.__loans.append(amount)
        self.__balance -= amount
        
    def transfer_money(self, amount, sender_account_no, receiver_account_no):
        sender_account = self.get_account(sender_account_no)
        receiver_account = self.get_account(receiver_account_no)

        if sender_account.balance < amount:
            raise Exception(f"Can't transfer the amount as it is more than the balance.")
        sender_account.withdraw(amount)
        receiver_account.deposit(amount)

    def check_admin(self, admin_pass):
        if self.__admin is None:
            raise Exception(f"Admin doesn't exist! Create an admin account first.")
        elif self.__admin.password != admin_pass:
            raise Exception(f"Incorrect password")

    def show_users(self, admin_pass):
        self.check_admin(admin_pass)
        return self.__accounts
    
    def delete_user_account(self, admin_pass, account_no):
        self.check_admin(admin_pass)
        account = self.get_account(account_no)
        self.__accounts = [ac for ac in self.__accounts if ac.account_no != account.account_no]
        return account

    def turn_off_loan(self, admin_pass):
        self.check_admin(admin_pass)
        self.__loan_active = False

    def turn_on_loan(self, admin_pass):
        self.check_admin(admin_pass)
        self.__loan_active = True

    def bankrupt_the_bank(self, admin_pass):
        self.check_admin(admin_pass)
        self.__is_bankrupt = True

    def total_balance(self, admin_pass):
        self.check_admin(admin_pass)
        return self.__balance
    
    def total_loan(self, admin_pass):
        self.check_admin(admin_pass)
        return sum(self.__loans)