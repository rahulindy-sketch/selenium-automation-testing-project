from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.saucedemo.com")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add Backpack to Cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Verify Cart Badge
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

if cart_badge.text == "1":
    print("✅ Test Passed - Product added to cart successfully")
else:
    print("❌ Test Failed")

driver.quit()