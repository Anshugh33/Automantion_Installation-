#import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By #class bhitra ko by vanne method provide gareko 

#open web page 
driver=webdriver.Chrome()

#go to url
driver.get("https://www.saucedemo.com/") 

#locate username field and pass values
driver.find_element(By.ID,"user-name").send_keys("standard_user")
print("entered usernamee")

#locate password field
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
print("entered password")

#click button 
driver.find_element(By.ID,"login-button").click()
print("logged in")

#verifying process
assert "inventory" in driver.current_url
print("Login Successful",driver.current_url)




