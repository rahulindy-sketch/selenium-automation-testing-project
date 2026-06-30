import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()

    # 🔥 FULL automation-safe Chrome mode
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")

    # IMPORTANT: stop password / security prompts
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    })

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.saucedemo.com")

    yield driver
    driver.quit()