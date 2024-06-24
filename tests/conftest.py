import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.login_page import LoginPage

load_dotenv()

DRIVER_PATH = os.getenv('DRIVER_PATH')


def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", help="Run tests in headless mode"
    )


@pytest.fixture(scope="session")
def driver(request):
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    driver_service = ChromeService(executable_path=DRIVER_PATH)
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)
