def test_login_page(setup):
    driver = setup

    username = driver.find_element("id", "user-name")
    password = driver.find_element("id", "password")
    login_button = driver.find_element("id", "login-button")

    assert username.is_displayed()
    assert password.is_displayed()
    assert login_button.is_displayed()