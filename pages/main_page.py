import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

load_dotenv()

DRIVER_PATH = os.getenv('DRIVER_PATH')
MAIN_PAGE = os.getenv('MAIN_PAGE')


class MainPage:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.login_button = (By.CSS_SELECTOR, "button[data-testid='authorization.button.guestUser']")
        self.url = MAIN_PAGE

    def open(self):
        self.driver.get(self.url)

    def get_login_button(self):
        return self.driver.find_element(*self.login_button)

    def click_login(self):
        self.get_login_button().click()


if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver_service = ChromeService(executable_path=DRIVER_PATH)
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    try:
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_login()
        time.sleep(1)
    finally:
        driver.quit()
