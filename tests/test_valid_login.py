from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

products = driver.find_element(By.CLASS_NAME, "title")

if products.text == "Products":
    print("✅ Test Passed - Valid Login Successful")
else:
    print("❌ Test Failed")

driver.quit()