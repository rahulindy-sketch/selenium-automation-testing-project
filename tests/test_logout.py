from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(setup):
    driver = setup
    wait = WebDriverWait(driver, 15)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait + open menu
    wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()

    # Wait for logout button fully visible (NOT just clickable)
    wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))).click()

    # IMPORTANT: wait for login page reset properly
    wait.until(EC.visibility_of_element_located((By.ID, "login-button")))

    assert driver.find_element(By.ID, "login-button").is_displayed()