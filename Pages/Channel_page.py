from Pages.Base_page import BasePage
from selenium.webdriver.common.by import By


class ChannelPage(BasePage):
    sport_channel_button = {"by": By.XPATH, "value": "//*[@id='root']/div/div/div/div/section[1]/div/div/div/div/ul/li[4"}
    play_button = {"by": By.CSS_SELECTOR, "value": "#root > div > div > div > div > section.page-tv-channels-list__content > div > div > div > a > div.tv-thumb__play-button"}
    subscribe_message = {"by": By.CLASS_NAME, "value": "player-stub__title"}

    def __init__(self,driver):
        self.driver = driver

    def _channel_method(self):
        self._select(self.sport_channel_button)
        self._select(self.play_button)
        return ChannelPage(self.driver)

    def subscribe_message_present(self):
        return self._presence(self.subscribe_message)


