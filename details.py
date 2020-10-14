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

class Credentials:

        """

        A class that generates new instances of logins
        """
        def __init__(self,username,password):
            self.username=username
            self.password=password

        credentials_list=[]

        def save_credentials(self):

            """Method that saves credential objects into credentials_list
            """
            Credentials.credentials_list.append(self)

        
        def delete_credential(self):

            """
            Method which deletes a particular credential
            """
            Credentials.credentials_list.remove(self)

        @classmethod
        def display_credential(cls):
            """
            method that returns the credential list
            """
            return cls.credentials_list



