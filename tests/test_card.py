from Pages.Home_page import HomePage
from Pages.Card_page import CardPage
from Pages.Account_page import AccountPage
from Pages.Subscribe_page import SubscribePage
import time
import pytest

"""test scenario: Open browser, navigate to ivi.ru homepage, try to sighn in with valid credentials,
   try to attach invalid credit_card, error msg must(При оплате возникла ошибка) present"""


class TestCardAttach:
    def test_search_result(self, browser):
        home_pg = HomePage(browser)
        time.sleep(10)
        home_pg.press_subscribe_button()
        sub_pg = SubscribePage(browser)
        sub_pg._subscribe_method_14()
        acc_pg=AccountPage(browser)
        acc_pg._valid_credentials_input("Sargis.1987@mail.ru", "10101010")
        card_pg=CardPage(browser)
        card_pg._invalid_card_req("5412 7534 5678 4417", "02/23", "785")

        assert card_pg.failure_message_present()=="При оплате возникла ошибка", "Wrong error msg is present"






