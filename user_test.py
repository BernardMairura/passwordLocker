import unittest # Importing the unittest module
from details import User # Importing the contact class

class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the user class behaviour
    """

    def setUp(self):
        """
        Set Up Method to run before each test case to check if the class has been instantiated correctly
        """
        self.new_user = User("Bern","Mairura","bmairura@gmail.com")

    def test_init(self):
        """
        Test to ensure that the object is initialized properly
        """
        self.assertEqual(self.new_user.first_name, "Bern")
        self.assertEqual(self.new_user.last_name, "Mairura")
        self.assertEqual(self.new_user.email, "bmairura@gmail.com")

    def test_save_user(self):
        """
        Method that tests wether an user credentials have been successfully saved
        """
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)


if __name__ == '__main__':
    unittest.main()