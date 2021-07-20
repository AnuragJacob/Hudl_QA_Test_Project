from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Chrome(executable_path='C:/Users/melab/OneDrive/Desktop/chromedriver.exe')
driver.maximize_window()
driver.get("https://www.hudl.com/login")
driver.find_element_by_id("logInWithOrganization").click()
driver.implicitly_wait(100)

driver.get("https://www.hudl.com/app/auth/login/organization")

email = "akj351@nyu.edu"
userName = driver.find_element_by_id("uniId_1")  
time.sleep(2)
userName.send_keys(email)

signIn = driver.find_element_by_xpath("//button[@data-qa-id='log-in-with-sso']")
signIn.click()
