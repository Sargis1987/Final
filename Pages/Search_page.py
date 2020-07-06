from Pages.Base_page import BasePage
from selenium.webdriver.common.by import By

"""Use Case: As a film fan, I want to have an oportunity to make a search, to find exactly what i want"""

class SearchPage(BasePage):
    find_search_message = {"by": By.CLASS_NAME, "value": "nbl-slimPosterBlock__title"}

    def __init__(self,driver):
        self.driver = driver

    def search_message_present(self):
        self._wait_visiable(self.find_search_message, 10)
        return self._find_els(self.find_search_message)