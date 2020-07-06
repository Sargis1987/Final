from Pages.Home_page import HomePage
from Pages.Account_page import AccountPage
import time

"""1. Open browser, navigate to ivi.ru homepage, try to sighn in with valid credentials,
   user.login must be shown in TestValidLogin-class"""
"""2. Open browser, navigate to ivi.ru homepage, try to sighn in with invalid username,
    (Неправильно указаны данные.) must be shown in TestInvalidUserLogin-class"""
"""3. Open browser, navigate to ivi.ru homepage, try to sighn in with valid username and 
     invalid password, user.login must be shown in TestValidLogin-class"""

class TestValidLogin:
    def test_valid_credentials(self, browser):
        home_pg=HomePage(browser)
        home_pg.press_account_button()
        acc_pg=AccountPage(browser)
        acc_pg._account_method_valid("Sargis.1987@mail.ru", "10101010")
        time.sleep(5)
        print(acc_pg.success_message_present())


        assert acc_pg.success_message_present()=="sargis.1987"

class TestInvalidUserLogin:
    def test_invalid_username(self, browser):
        home_pg=HomePage(browser)
        home_pg.press_account_button()
        acc_pg=AccountPage(browser)
        acc_pg._invalid_usercred_input("Sargis.1987@mail")

        assert acc_pg.uname_failure_message_present()== "Неправильно указаны данные."

class TestInvalidPassLogin:
    def test_invalid_password(self, browser):
        home_pg=HomePage(browser)
        home_pg.press_account_button()
        acc_pg=AccountPage(browser)
        acc_pg._account_method_valid("Sargis.1987@mail.ru", "101010")

        assert acc_pg.pass_failure_message_present() == "Неверно указан пароль. Пожалуйста, попробуйте еще раз"




