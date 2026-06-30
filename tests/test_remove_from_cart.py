from selenium.webdriver.common.by import By

def test_remove_from_cart(setup):
    driver = setup

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add product to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Remove product from cart
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    # Verify cart badge is removed
    cart_badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

    assert len(cart_badges) == 0