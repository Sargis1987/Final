from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
import pytest


"""Use Case: As a film fan, I want to have my own account, in order to save my playlists"""
"""Open browser, navigate to ivi.ru homepage, try to sighn in with valid credentials"""

driver=webdriver.Chrome(executable_path="..//driver/chromedriver.exe")
driver.get("https://www.ivi.ru/")
#driver.maximize_window()
#print(driver.title)
#print(driver.current_url)
#driver.execute_script("window.scrollBy(0,6000)","")
time.sleep(3)
#iframes=driver.find_elements(By.TAG_NAME,"iframe")
#print(len(iframes))
#driver.switch_to.frame(iframes[8])
#time.sleep(10)
driver.find_element(By.XPATH,"/html/body/header/div/div[2]/span").click()
time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div[1]").click()
driver.find_element(By.ID,"jsAuthToken").click()
print("User input field enabled:", driver.find_element(By.ID,"jsAuthToken").is_enabled())
driver.find_element(By.XPATH,"//*[@id='jsAuthToken']/div/div[1]/input").clear()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='jsAuthToken']/div/div[1]/input").send_keys("Sargis.1987@mail.ru")
driver.find_element(By.CSS_SELECTOR,"#jsAuthToken > div > div.auth-block__state-container.state-container > button").click()
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='jsEmailAuth']/div/div[1]/input").click()
print("Pass input field enabled:", driver.find_element(By.XPATH,"//*[@id='jsEmailAuth']/div/div[1]/input").is_enabled())
driver.find_element(By.XPATH,"//*[@id='jsEmailAuth']/div/div[1]/input").send_keys("10101010")
driver.find_element(By.XPATH,"//*[@id='jsEmailAuth']/div/div[2]/button").click()
time.sleep(10)
iframes=driver.find_elements(By.TAG_NAME,"iframe")
print(len(iframes)) # here code must be  refactored in order to get the iframe name
driver.switch_to.frame("js-buy-iframe")
driver.find_element(By.CLASS_NAME,"card-number").click()
driver.find_element(By.CLASS_NAME,"js-card-number").send_keys("5412 7534 5678 4417")
driver.find_element(By.CLASS_NAME,"card-data").click()
time.sleep(2)
driver.find_element(By.NAME,"DATE").send_keys("02/23")
driver.find_element(By.CLASS_NAME,"card-code").click()
driver.find_element(By.NAME,"secure_code").send_keys("785")
driver.find_element(By.ID,"pay-submit").click()
time.sleep(10)
iframes=driver.find_elements(By.TAG_NAME,"iframe")
print(len(iframes))
driver.switch_to.default_content()
assert (driver.find_element(By.XPATH,"//*[@id='modal-container']/div/div/div/span[1]").text
    =="Оплата не прошла"), "valid card was attached"


"""for k in range(len(iframes)+1):
    driver.switch_to.frame(str(iframes))
    try:
        driver.find_element(By.XPATH,"/html/body/div[1]/div/section[1]/div/div/div/div[1]/a").click()
    except NoSuchElementException:
        k+=1
    """


#driver.find_element(By.XPATH,"/html/body/div[1]/div/section[1]/div/div/div/div[1]/a").click()

time.sleep(5)
driver.execute_script("window.scrollBy(0,10000)","")
#driver.find_element(By.LINK_TEXT,"О компании").click()