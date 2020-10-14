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


def delete_user(user):
    """
    Function to delete a user
    """
    user.delete_user()

def display_user():
    """
    Function that returns saved users
    """
    return User.display_users()