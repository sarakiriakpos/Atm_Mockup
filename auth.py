
import random
import validation
import database
from getpass import getpass

def init():
    print("Welcome! This is the People's Bank!")

    createAccount = int(input("Do you have an existing account with us?: 1 (yes) 2 (no) \n"))

    if createAccount == 1:

        login()

    elif createAccount == 2:

        register()

    else:
        print("The option you selected is invalid!")
        init()


def login():
    print("********* Login ***********")

    userAccountNumber = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(
        userAccountNumber)

    if is_valid_account_number:

        password = getpass("Please, enter your password \n")

        user = database.authenticated_user(userAccountNumber, password)

        if user:
            bank_operation(user)

        print("The account or password you entered is invalid")
        login()

    else:
        print(
            "Account Number Invalid: Please, check if your account is up to 10 digits and only numbers.")
        init()


def register():
    print("****** Register *******")

    email = input("Enter your email address? \n")
    firstName = input("Enter your first name? \n")
    lastName = input("Enter your last name? \n")
    password = getpass("Create your password. \n")

    accountNumber = generation_account_number()

    is_user_created = database.create(
        accountNumber, firstName, lastName, email, password)

    if is_user_created:

        print("Congratulation, Your Account is successfully created!")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % accountNumber)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input(
        "What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation():
    print("withdrawal")
   

def deposit_operation():
    print("Deposit Operations")


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()


init()
