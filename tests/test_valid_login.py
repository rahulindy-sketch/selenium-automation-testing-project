from selenium.webdriver.common.by import By

def test_valid_login(setup):
    driver = setup

    # Login with valid credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verify successful login
    products_title = driver.find_element(By.CLASS_NAME, "title")

    assert products_title.text == "Products"