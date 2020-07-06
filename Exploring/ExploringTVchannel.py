from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

"""Use Case: As a user, I want to have chance to watch my favorite sport programs"""
"""Open browser, navigate to ivi.ru homepage, choose tv-channels"""

driver=webdriver.Chrome(executable_path="..//driver/chromedriver.exe")
driver.get("https://www.ivi.ru/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/header/div/nav/ul[1]/li[5]/a").click()
print(driver.current_url)
print(driver.title)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/section[1]/div/div/div/div/ul/li[4]").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#root > div > div > div > div > section.page-tv-channels-list__content > div > div > div > a > div.tv-thumb__play-button").click()
time.sleep(5)
assert (driver.find_element(By.CLASS_NAME,"player-stub__title").text
      =="Подписка ivi теперь с ТВ-каналами по старой цене"), "Not the Expected text"
driver.quit()
