from selenium import webdriver
from loginpage import LoginPage
import time 


driver=webdriver.Chrome()
driver.get("http://www.saucedemo.com/")
  
login_page = LoginPage(driver)
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login()

time.sleep(11)  

assert "inventory" in driver.current_url
print("Login successful, inventory page reached")
driver.quit()