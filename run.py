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

def display_user():
    """
    Function that returns saved users
    """
    return User.display_users()


def delete_user(User):
    """
    Function to delete a user
    """
    User.delete_user()

