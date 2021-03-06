from details import User
from details import Credentials
import random

# user area
def create_user(fname, lname, email):
    """
    Function to create a new user
    """
    new_user = User(fname, lname, email)
    return new_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user_details()

def display_user(user):
    """
    Function that returns saved users
    """
    return user.display_users()


def delete_user(user):
    """
    Function to delete a user
    """
    user.delete_user()


#credentials area

def create_credential(username, password):
    """
    Function to create new user credentials
    """
    new_credential = Credentials(username, password)
    return new_credential

def save_credential(Credentials):
    """
    Function to save user credentials
    """
    Credentials.save_credential()

def display_credential():
    """
    function that returns saved user credentials
    """
    return Credentials.display_credential()

def delete_credential(Credentials):
    """
    Function to delete all users credentials
    """
    Credentials.delete_credential()


def main():

    print("Password Locker.Select your desired  action")

    while True:
        print("Actions: \n nu - create a new user account \n pa - password account\n ad - display account \n ex -exit  \n")

        short_code = input().lower()
        
        if short_code == 'nu':
            print("New User")
            print("-"*10)
            print("please create your prefered site account")
            site = input()
            print(f" welcome to {site} account")

            print("First name ....")
            fname = input()

            print("Last name ...")
            lname = input()

            print("Email address ...")
            email = input()

            print("Enter username ...")
            username = input()

            print("Enter Password ...")
            password = input()

            save_user(create_user(fname, lname,email))  # creates and saves new user.
            save_credential(create_credential(username, password))  # creates and saves credentials for the new user.
            print('\n')
            print(f" A new {site} account by {fname} {lname} has successfully been created")
            print(f" The username is {username} and the password is {password}")
            print('\n')

        elif short_code == 'pa':
            print("New User")
            print("-" * 10)
            print("please create your prefered site account")
            site = input()
            print(f"Welcome to {site} account")

            print("First name ....")
            fname = input()

            print("Last name ...", )
            lname = input()

            print("Email address ...")
            email = input()

            print("Enter username ... (a password will be generated for you...)")
            username = input()

            s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?"
            password = "".join(random.sample(s, 7))

            save_user(create_user(fname,lname,email))  # create and save new user account.
            save_credential(create_credential(username, password))  # create and save a password.
            print('\n')
            print(f" New {site} account by {fname} {lname} created successfully")
            print(f" Your {username} and  password is {password}")
            print('\n')
        elif short_code == 'ad':

            if display_user():
                print("List of your accounts")
                print('\n')

                for user in display_users():
                    print(f"{user.first_name} {user.last_name} has an account for {site}")

                print('\n')
            else:
                print('\n')
                print("You don't have an existing account")
                print('\n')

        elif short_code == "ex":
            print(":/ Come back again...")
            break
    else:
        print(" :( please key in allowed options only !!")
        







if __name__ == '__main__':
    main()





