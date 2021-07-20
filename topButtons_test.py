from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path='C:/Users/melab/OneDrive/Desktop/chromedriver.exe')
driver.maximize_window()
driver.get("https://www.hudl.com/login")


## to check if the Back button and the Hudl logo button (both redirect to same page) are working properly ##
driver.find_element_by_class_name("icon-back").click()
print("Clicked Back Button")
time.sleep(1)

driver.get("https://www.hudl.com/login")
driver.find_element_by_class_name("icon-logomark").click()
print("Clicked Hudl Logo Button")
time.sleep(2)

## to check if the Sign Up button works properly ##
driver.get("https://www.hudl.com/login")
signUp = driver.find_element_by_xpath('//a[@href="/register/signup"]')
time.sleep(2)
signUp.click()
print("Clicked Sign Up Button")

