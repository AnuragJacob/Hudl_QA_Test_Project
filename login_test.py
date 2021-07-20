from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='C:/Users/melab/OneDrive/Desktop/chromedriver.exe')
driver.maximize_window()
driver.get("https://www.hudl.com/login")

## To check if login was successful ##
def checkError():
    error_message = "We didn't recognize that email and/or password."
    errors = driver.find_elements_by_class_name("login-error-container")
    # if we find that error message within errors, then login has failed
    if any(error_message in e.text for e in errors):
        print("[!] Login failed")
    else:
        print("[+] Login successful")

## Check for positive and negative test cases

## 1. Correct username and incorrect password
email = "akj351@nyu.edu"
pw = "123456"
userName = driver.find_element_by_name("username")  
userName.send_keys(email)
passWord = driver.find_element_by_name("password")  
passWord.send_keys(pw)
time.sleep(3)
signIn = driver.find_element_by_id("logIn").click()
time.sleep(3)
checkError()
driver.refresh()

##2. Blank user name and password
email = ""
pw = ""
userName = driver.find_element_by_name("username")  
userName.send_keys(email)
passWord = driver.find_element_by_name("password")  
passWord.send_keys(pw)
time.sleep(3)
driver.find_element_by_id("logIn").click()
time.sleep(3)
checkError()
# driver.refresh()

## 3. Correct username and incorrect password
email = "akj351@nyu.edu"
pw = "Anurag2021"
userName = driver.find_element_by_name("username")  
userName.send_keys(email)
passWord = driver.find_element_by_name("password")  
passWord.send_keys(pw)
time.sleep(3)
driver.find_element_by_id("logIn").click()
checkError()