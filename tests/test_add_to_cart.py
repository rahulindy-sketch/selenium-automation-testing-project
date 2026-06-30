from selenium.webdriver.common.by import By

def test_add_to_cart(setup):
    driver = setup

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add product to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Verify cart badge
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert cart_badge.text == "1"