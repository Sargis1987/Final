from Pages.Base_page import BasePage
from selenium.webdriver.common.by import By
from Pages.Account_page import AccountPage
from Pages.Search_page import SearchPage
from Pages.Subscribe_page import SubscribePage
from Pages.Channel_page import ChannelPage


class HomePage(BasePage):
    channel_button = {"by": By.XPATH, "value": "/html/body/header/div/nav/ul[1]/li[5]/a"}
    users_button = {"by": By.XPATH, "value": "/html/body/header/div/div[4]/span/a"}
    subscribe_button = {"by": By.XPATH, "value": "/html/body/header/div/div[2]/span"}
    search_button = {"by": By.ID, "value": "js-quick-search-form"}
    search_field = {"by": By.ID, "value": "search-text"}
    title_to_search=("Царство небесное")

    def __init__(self, driver):
        self.driver = driver

    def press_account_button(self):
        self._wait_clickable(self.users_button, 10)
        self._select(self.users_button)
        return AccountPage(self.driver)


    def press_subscribe_button(self):
        self._wait_clickable(self.subscribe_button, 10)
        self._select(self.subscribe_button)
        return SubscribePage(self.driver)

    def press_channel_button(self):
        self._select(self.channel_button)
        return ChannelPage(self.driver)

    def make_search(self):
        self._select(self.search_button)
        self._select(self.search_field)
        self._input(self.search_field, self.title_to_search)
        self._press_enter(self.search_field)
        return SearchPage(self.driver)


