from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/download")

driver.find_element("link text","some-file.txt").click() #THIS WILL DOWNLOAD FILE
time.sleep(5)
print("file downloaded")

driver.quit()