from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

checkbox1=driver.find_element(By.XPATH,"//input[@type='checkbox'][1]")
checkbox2=driver.find_element(By.XPATH,"//input[@type='checkbox'][2]")

checkbox2.click()

print("checkbox 1 is selected:", checkbox1.is_selected())
print("checkbox 2 is selected:", checkbox2.is_selected())

driver.quit()

