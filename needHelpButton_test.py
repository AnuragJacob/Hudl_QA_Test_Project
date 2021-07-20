from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='C:/Users/melab/OneDrive/Desktop/chromedriver.exe')
driver.maximize_window()
driver.get("https://www.hudl.com/login")

## To check if login was successful ##
def checkError():
    error_message = "That email address doesn't exist in Hudl. Check with your coach to ensure they have the right email address for you."
    errors = driver.find_elements_by_class_name("reset-error-container")
    # if we find that error message within errors, then login has failed
    if any(error_message in e.text for e in errors):
        print("[!] Reset failed")
    else:
        print("[+] Reset email has been sent")



## to check if Need Help button is working properly ##
time.sleep(3)
driver.find_element_by_class_name("need-help").click()
time.sleep(3)
print("Clicked Need Help Button")
# element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "[@id='forgot-email']")))

## After clicking on Need Help, we come to another page. We test the functionality of this page ##

## Negative test - Reset password for non-existent email
email = "abcd@nyu.edu"
userName = driver.find_element_by_id("forgot-email")  
userName.send_keys(email)
time.sleep(3)
needHelp = driver.find_element_by_id("resetBtn").click()
time.sleep(3)
checkError()
userName.clear()


## Positive test - Reset password for existing email
email = "akj351@nyu.edu"
registerID = driver.find_element_by_id("forgot-email") 
registerID.send_keys(email)
time.sleep(2)
needHelp = driver.find_element_by_id("resetBtn").click()
checkError()



