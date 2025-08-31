from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown=Select(driver.find_element(By.ID,"dropdown"))
dropdown.select_by_visible_text("option 1")

time.sleep(3)
driver.quit()