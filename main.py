from bank import Bank
from time import sleep

my_bank = Bank()

logged_in = {
    'user': None,
    'admin': None
}

def user_login():
    print("-------- Account Types -----")
    print("|   [1] Savings Account    |")
    print("|   [2] Current Account    |")
    print("----------------------------")
    account_type = None
    while account_type is None:
        option = input("Enter account option no: ")
        if option == '1': 
            account_type = "SAVINGS"
        elif option == '2':
            account_type = "CURRENT"
        else:
            print(f"Invalid type no: '{option}'")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    account = my_bank.create_account(name, email, address, account_type)
    logged_in["user"] = account
    print(f"Congrats! Account was successfully created")
    print(account)
    user_do()

def admin_login():
    if my_bank.admin is None:
        name = input("Enter your name: ")
        password = input("Enter a password: ")
        logged_in["admin"] = my_bank.create_admin(name, password)
        print("Congrats! Admin is successfully created.")
    else:
        isCorrect = False
        print("--------------- Admin Login ---------------")
        while isCorrect is False:
            password = input("Enter the admin password: ")
            isCorrect = password == my_bank.admin.password
            if isCorrect is False:
                print("Wrong password! try again.")
            else: 
                logged_in["admin"] = my_bank.admin
                print(f"welcome, {logged_in['admin'].name}, take a seat and do the job.")
    admin_do()

def login():
    print("---------- Login Options ---------")
    print("|   [1] Create a bank account    |")
    print("|   [2] Login/Signup as admin    |")
    print("|   [3] Exit                     |")
    print("----------------------------------")
    option = input("Enter the option no: ")
    if option == '1':
        user_login()
    elif option == '2':
        admin_login()
    elif option == '3':
        exit()
    else:
        raise Exception(f"Invalid option no: {option}")

def logout():
    logged_in['user'] = None
    logged_in['admin'] = None

def user_deposit():
    amount = int(input("Enter the amount to deposit: "))
    my_bank.deposit(logged_in["user"].account_no, amount)
    print(f"Congrats! successfully deposited BDT {amount}")

def user_withdraw():
    amount = int(input("Enter the amount to withdraw: "))
    my_bank.withdraw(logged_in["user"].account_no, amount)
    print(f"Congrats! successfully withdrawn BDT {amount}")

def user_balance():
    balance = my_bank.get_account(logged_in["user"].account_no).balance
    print(f"available balance: {balance}")

def user_transactions():
    transactions = my_bank.get_account(logged_in["user"].account_no).transactions
    print("------------- Transactions History -----------------")
    for amount in transactions:
        if amount < 0:
            print(f"   -{abs(amount)} (Out)")
        else:
            print(f"   +{abs(amount)} (In)")
    print("----------------------------------------------------")

def user_loan():
    amount = int(input("Enter the loan amount: "))
    my_bank.take_loan(logged_in["user"].account_no, amount)
    print(f"Congrats! successfully took loan of amount BDT {amount}")

def user_transfer():
    account_no = input("Enter the receivers account no: ")
    receiver = my_bank.get_account(account_no)
    amount = int(input("Enter the amount to transfer: "))
    my_bank.transfer_money(amount, logged_in["user"].account_no, account_no)
    print(f"Congrats! successfully transferred the amount BDT {amount} to the receiver '{receiver.account_no}'")

def user_do():
    print("------------ User Options ------------")
    print("|   [1] Deposit                      |")
    print("|   [2] Withdraw                     |")
    print("|   [3] Check available balance      |")
    print("|   [4] See transaction history      |")
    print("|   [5] Take a loan                  |")
    print("|   [6] Transfer money               |")
    print("|   [7] Logout                       |")
    print("--------------------------------------")
    option = input("Enter the option no: ")
    if option == '1':
        user_deposit()
    elif option == '2':
        user_withdraw()
    elif option == '3':
        user_balance()
    elif option == '4':
        user_transactions()
    elif option == '5':
        user_loan()
    elif option == '6':
        user_transfer()
    elif option == '7':
        logout()
    else:
        raise Exception(f"Invalid option no: {option}")

def admin_see_all_users():
    accounts = my_bank.show_users(logged_in["admin"].password)
    print("-------------- All Users List ----------------")
    for account in accounts:
        print(account)
        print("---------------------------------------------")
    if len(accounts) < 1:
        print("       No Users          ")

def admin_delete_user():
    account_no = input("Enter the account no of the user you want to delete: ")
    my_bank.delete_user_account(logged_in["admin"].password, account_no)
    print(f"User '{account_no}' is deleted successfully")

def admin_check_balance():
    balance = my_bank.total_balance(logged_in["admin"].password)
    print(f"total balance: {balance}")

def admin_check_loan():
    loan = my_bank.total_loan(logged_in["admin"].password)
    print(f"total loan given: {loan}")

def admin_switch_loan_feature():
    is_loan_active = my_bank.is_loan_active
    if is_loan_active:
        print("Loan is currently active, turning off the feature...")
        my_bank.turn_off_loan(logged_in["admin"].password)
        sleep(0.5)
        print("Success! Loan is deactivated.")
    else:
        print("Loan is currently inactive, turning on the feature...")
        my_bank.turn_on_loan(logged_in["admin"].password)
        sleep(0.5)
        print("Success! Loan is activated.")

def admin_bankrupt():
    my_bank.bankrupt_the_bank(logged_in["admin"].password)
    print("(hold on) Entering the bank...")
    sleep(0.5)
    print("(hold on) Threatening the existing people to leave...")
    sleep(0.5)
    print("(hold on) Taking some money first for us...")
    sleep(0.5)
    print("(hold on) Telling the founders to go away with the money...")
    sleep(0.5)
    print(" :) Founders are gone with the money...")
    print(" :) guess what?         Bank is bankrupted! People are gonna die bruh :) ")

def admin_do():
    print("------------- Admin Options -----------------")
    print("|   [1] See all users in the bank           |")
    print("|   [2] Delete an user account              |")
    print("|   [3] Check total balance of the bank     |")
    print("|   [4] Check total loan of the bank        |")
    print("|   [5] Switch the loan feature (ON/OFF)    |")
    print("|   [6] Bankrupt the bank                   |")
    print("|   [7] Logout                              |")
    print("---------------------------------------------")
    option = input("Enter the option no: ")
    if option == '1':
        admin_see_all_users()
    elif option == '2':
        admin_delete_user()
    elif option == '3':
        admin_check_balance()
    elif option == '4':
        admin_check_loan()
    elif option == '5':
        admin_switch_loan_feature()
    elif option == '6':
        admin_bankrupt()
    elif option == '7':
        logout()
    else:
        print(f"Invalid option no: {option}")

while True:
    try:
        if logged_in['user'] is not None:
            user_do()
        elif logged_in['admin'] is not None:
            admin_do()
        else:
            login()
    except Exception as err:
        print(err)