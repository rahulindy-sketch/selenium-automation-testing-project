from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("wrong_password")
driver.find_element(By.ID, "login-button").click()

error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")

if error.is_displayed():
    print("✅ Test Passed - Error message displayed for invalid login")
else:
    print("❌ Test Failed")

driver.quit()