from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

"""Use Case: As a film fan, I want to have an oportunity to make a search, to find exactly what i want"""
"""Open browser, navigate to ivi.ru homepage, input name Kingdom of Heaven in searchbox"""

driver=webdriver.Chrome(executable_path="..//driver/chromedriver.exe")
driver.get("https://www.ivi.ru/")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.find_element(By.ID,"js-quick-search-form").click()
driver.find_element(By.ID,"search-text").send_keys("Царство небесное")
driver.find_element(By.ID,"search-text").send_keys(Keys.ENTER)
time.sleep(5)
assert (driver.find_element(By.XPATH, "//*[@id='js-search-page']/div/section[1]/div/li[1]/a/div[2]/div[1]").text
        =="Царство небесное"), "The name searched not present"
driver.quit()
