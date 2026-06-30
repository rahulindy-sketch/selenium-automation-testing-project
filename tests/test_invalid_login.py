from selenium.webdriver.common.by import By

def test_invalid_login(setup):
    driver = setup

    # Enter invalid credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    # Capture error message
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")

    assert error.is_displayed()