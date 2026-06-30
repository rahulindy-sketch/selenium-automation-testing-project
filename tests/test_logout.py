from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.saucedemo.com")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Open menu
driver.find_element(By.ID, "react-burger-menu-btn").click()

# WAIT for menu animation
time.sleep(2)

# Click logout
driver.find_element(By.ID, "logout_sidebar_link").click()

# Verify logout
login_button = driver.find_element(By.ID, "login-button")

if login_button.is_displayed():
    print("✅ Test Passed - Logout successful")
else:
    print("❌ Test Failed")

driver.quit()