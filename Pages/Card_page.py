from Pages.Base_page import BasePage
from selenium.webdriver.common.by import By

"""Use Case: As a film fan, I want to attach my bank-card, in order to view certain films"""

class CardPage(BasePage):
    frame_find = {"by": By.TAG_NAME, "value": "iframe"}
    frame_name=("js-buy-iframe")
    card_number_button = {"by": By.CLASS_NAME, "value": "card-number"}
    card_number_input={"by": By.CLASS_NAME, "value": "js-card-number"}
    card_date_button = {"by": By.CLASS_NAME, "value": "card-data"}
    card_date_input={"by": By.NAME, "value": "DATE"}
    card_code_button = {"by": By.NAME, "value": "secure_code"}
    card_code_input={"by": By.NAME, "value": "secure_code"}
    card_register_button={"by": By.ID, "value": "pay-submit"}
    invalid_attach_back_button = {"by": By.XPATH, "value": "//*[@id='modal-container']/div/div/div/div"}
    invalid_attach_error_msg = {"by": By.XPATH, "value": "//*[@id='modal-container']/div/div/div/span[2]/span"}


    def __init__(self,driver):
        self.driver = driver

    def _invalid_card_req(self, card_number, exp_date, secure_code):
        self._wait_visiable(self.frame_find, 10)
        self._find_els(self.frame_find)
        self._switch_frame(self.frame_name)
        self._select(self.card_number_button)
        self._input(self.card_number_input, card_number)
        self._select(self. card_date_button)
        self._input(self.card_date_input, exp_date)
        self._wait_clickable(self.card_code_button, 10)
        self._select(self.card_code_button)
        self._input(self.card_code_input, secure_code)
        self._select(self.card_register_button)
        self._switch_to_default_frame()
        return CardPage(self.driver)

    def failure_message_present(self):
        self._wait_visiable(self.invalid_attach_back_button, 10)
        self._find(self.invalid_attach_back_button)
        return self._find(self.invalid_attach_error_msg).text

