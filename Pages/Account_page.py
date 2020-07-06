from Pages.Base_page import BasePage
from selenium.webdriver.common.by import By

"""Use Case: As a film fan, I want to have my own account, in order to save my playlists, be able tu subscribe"""


class AccountPage(BasePage):
    sighnin_button = {"by": By.XPATH, "value": "//*[@id='root']/div/div/div/div/button"}
    login_form = {"by": By.ID, "value": "jsAuthToken"}
    username_input = {"by": By.XPATH, "value": "//*[@id='jsAuthToken']/div/div[1]/input"}
    password_input = {"by": By.XPATH, "value": "//*[@id='jsEmailAuth']/div/div[1]/input"}
    uname_continue_button = {"by": By.CSS_SELECTOR, "value": "#jsAuthToken > div > div.auth-block__state-container.state-container > button"}
    pass_continue_button = {"by": By.CSS_SELECTOR, "value": "#jsEmailAuth > div > div.auth-password-block__state-container.state-container > button"}
    login_success_message = {"by": By.XPATH, "value": "//*[@id='root']/div/div[2]/div/div[1]/span[1]"}
    uname_failure_message ={"by": By.XPATH, "value": "//*[@id='jsAuthToken']/div/div[1]/div/div"}
    pass_failure_message = {"by": By.XPATH, "value": "//*[@id='jsEmailAuth']/div/div[1]/div/div"}

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def _account_method_valid(self, username, password): #this method is used in test_card
        self._wait_clickable(self.sighnin_button, 10)
        self._select(self.sighnin_button)
        self._wait_clickable(self.login_form, 10)
        self._select(self.login_form)
        self._wait_clickable(self.username_input, 10)
        self._input(self.username_input, username)
        self._wait_clickable(self.uname_continue_button, 10)
        self._select(self.uname_continue_button)
        self._wait_visiable(self.password_input, 10)
        self._input(self.password_input, password)
        self._wait_clickable(self.pass_continue_button, 10)
        self._select(self.pass_continue_button)
        return AccountPage(self.driver)

    def _valid_credentials_input(self, username, password):
        self._wait_clickable(self.login_form, 10)
        self._select(self.login_form)
        self._wait_clickable(self.username_input, 10)
        self._input(self.username_input, username)
        self._wait_clickable(self.uname_continue_button, 10)
        self._select(self.uname_continue_button)
        self._wait_visiable(self.password_input, 10)
        self._input(self.password_input, password)
        self._wait_clickable(self.pass_continue_button, 10)
        self._select(self.pass_continue_button)
        return AccountPage(self.driver)


    def _invalid_usercred_input(self, username):
        self._wait_clickable(self.sighnin_button, 10)
        self._select(self.sighnin_button)
        self._wait_clickable(self.login_form, 10)
        self._select(self.login_form)
        self._wait_clickable(self.username_input, 10)
        self._input(self.username_input, username)
        self._wait_clickable(self.uname_continue_button, 10)
        self._select(self.uname_continue_button)
        self._wait_visiable(self.uname_failure_message, 10)

    def _invalid_passcred_input(self, username, password):
        self._wait_clickable(self.login_form, 10)
        self._select(self.login_form)
        self._wait_clickable(self.username_input, 10)
        self._input(self.username_input, username)
        self._wait_clickable(self.uname_continue_button, 10)
        self._select(self.uname_continue_button)
        self._wait_visiable(self.password_input, 10)
        self._input(self.password_input, password)

    def success_message_present(self):
        print("Now you are logged in")
        return self._find(self.login_success_message).text

    def uname_failure_message_present(self):
        self._wait_visiable(self.uname_failure_message, 10)
        print("The username is invalid")
        return self._find(self.uname_failure_message).text

    def pass_failure_message_present(self):
        self._wait_visiable(self.pass_failure_message, 10)
        print("The password is invalid")
        return self._find(self.pass_failure_message).text




