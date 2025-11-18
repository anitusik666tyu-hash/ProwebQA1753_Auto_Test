import pytest
from selenium import webdriver

@pytest.fixture
def driver_chrome():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("==no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service = Service(ChromeDriverManager().install()),
        options = options
    )
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver


# @pytest.fixture
# def driver_firefox():
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver


# @pytest.fixture
# def driver_edge():
#     driver = webdriver.Edge()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver

