class User:

    """

    A class that generates new instances of contacts
    """
    users_list=[]

    def __init__ (self,first_name,last_name,email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
       
        
   

    def save_user(self):
        """
        save user details method which saves users to the user list and edits(appends)them
        """
        User.users_list.append(self)

    @classmethod
    def display_users(cls):
        return cls.display_users