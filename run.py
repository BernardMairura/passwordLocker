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

def save_user(User):
    """
    Function to save user
    """
    User.save_user_details()

def display_user(User):
    """
    Function that returns saved users
    """
    return User.display_users()


def delete_user(User):
    """
    Function to delete a user
    """
    User.delete_user()


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







if __name__ == '__main__':
    main()





