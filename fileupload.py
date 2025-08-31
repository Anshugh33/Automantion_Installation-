from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

file_input=driver.find_element(By.ID, "file-upload")
file_input.send_keys("C:\Users\User\Downloads\some-file (1).txt") #path milauna baki 

driver.find_element(By.ID,"file-submit").click()
time.sleep(2)
print("file is uploaded")

driver.quit()