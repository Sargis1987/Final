from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest


"""Use Case: As a film fan, I want to have my own account, in order to save my playlists"""
"""Open browser, navigate to ivi.ru homepage, try to sighn in with valid credentials"""

driver=webdriver.Chrome(executable_path="..//driver/chromedriver.exe")
driver.get("https://www.ivi.ru/")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, '/html/body/header/div/div[4]/span/a').click() #must include comment Why Xpath was choosen
driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/button").click()
assert (driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/button/span[2]").text
        =="Войти или зарегистрироваться"),  "Invalid Name of button"
driver.find_element(By.ID,"jsAuthToken").click()
print("User input field enabled:", driver.find_element(By.ID,"jsAuthToken").is_enabled())
driver.find_element(By.XPATH,"//*[@id='jsAuthToken']/div/div[1]/input").clear()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='jsAuthToken']/div/div[1]/input").send_keys("Sargis.1987@mail.ru")
driver.find_element(By.CSS_SELECTOR,"#jsAuthToken > div > div.auth-block__state-container.state-container > button").click()
driver.find_element(By.XPATH,"//*[@id='jsEmailAuth']/div/div[1]/input").click()
print("Pass input field enabled:", driver.find_element(By.XPATH,"//*[@id='jsEmailAuth']/div/div[1]/input").is_enabled())
driver.find_element(By.XPATH,"//*[@id='jsEmailAuth']/div/div[1]/input").send_keys("10101010")
driver.find_element(By.XPATH,"//*[@id='jsEmailAuth']/div/div[2]/button").click()
driver.find_element(By.XPATH,"//*[@id='modal-container']/div[2]/div/div/div/div[2]/div").click()
print(driver.title)
print(driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div[1]/span[1]").text)
assert (driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div[1]/span[1]").text
        =="sargis.1987")

time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='root']/div/section/div/div/div[1]/ul[3]/li[2]/a").click()
assert (driver.find_element(By.XPATH, "//*[@id='root']/div/div/section[2]/div/div/div").text
        =="Здесь будут фильмы, которые вы решите посмотреть позже"), "Invalid Text"
driver.close()
