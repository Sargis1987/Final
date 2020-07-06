from Pages.Base_page import BasePage
from selenium.webdriver.common.by import By
from Pages.Account_page import AccountPage


class SubscribePage(BasePage):
    try14_button = {"by": By.XPATH, "value": "//*[@id='root']/div/div[2]/div[2]/div/div[1]"}
    subscribe_button = {"by": By.XPATH, "value": "/html/body/header/div/div[2]/span"}

    def _subscribe_method_14(self):
        self._wait_clickable(self.try14_button, 15)
        self._select(self.try14_button)
        return AccountPage(self.driver)

    def press_subscribe_button(self):
        self._wait_clickable(self.subscribe_button, 10)
        self._select(self.subscribe_button)
        return SubscribePage(self.driver)