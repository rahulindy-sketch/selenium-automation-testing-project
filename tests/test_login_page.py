from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.saucedemo.com")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

if username.is_displayed() and password.is_displayed() and login_button.is_displayed():
    print("✅ Test Passed - Login page loaded successfully")
else:
    print("❌ Test Failed")

driver.quit()