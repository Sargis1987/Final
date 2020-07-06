from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""" In this page the main functionality to interact with web_app ivi.ru is grouped"""

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _maximize(self):
        self.driver.maximize_window()

    def _url_title_get(self):
        return self.driver.current_url

    def _open_url(self, url):
        self.driver.get(url)

    def _find(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _find_els(self, locator):
        return self.driver.find_elements(locator['by'], locator['value'])

    def _switch_frame(self, frname):
        self.driver.switch_to.frame(frname)

    def _switch_to_default_frame(self):
        self.driver.switch_to.default_content()

    def _select(self, locator):
        self._find(locator).click()

    def _clear(self, locator):
        self._find(locator).clear()

    def _input(self, locator, typetext):
        self._find(locator).send_keys(typetext)

    def _press_enter(self, locator):
        self._find(locator).send_keys(Keys.ENTER)

    def _presence(self, locator):
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _wait_clickable(self, locator, seconds=0):
        if seconds>0:
            try:
                wait = WebDriverWait(self.driver, seconds)
                wait.until(EC.element_to_be_clickable((locator['by'], locator['value'] )))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return False


    def _wait_visiable(self, locator, seconds=0):
        if seconds>0:
            try:
                wait = WebDriverWait(self.driver, seconds)
                wait.until(EC.visibility_of_element_located((locator['by'], locator['value'] )))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return False
