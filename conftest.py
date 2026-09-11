import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    # Setup Chrome WebDriver options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    yield driver

    # Teardown: close browser sessions
    driver.quit()
