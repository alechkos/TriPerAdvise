import unittest
import menu_login_signup


class Menu_login_signup(unittest.TestCase):
    def test_mail_is_valid(self):
        self.assertTrue(menu_login_signup.mail_is_valid('1111@sus.com'), 'Incorrect mail')
        self.assertTrue(menu_login_signup.mail_is_valid('1@mail.com'), 'Incorrect mail')
        self.assertTrue(menu_login_signup.mail_is_valid('1234@mail.com'), 'Incorrect mail')
        self.assertTrue(menu_login_signup.mail_is_valid('1234@mail.com'), 'Incorrect mail')


if __name__ == '__main__':
    unittest.main()
