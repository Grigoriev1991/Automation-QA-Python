import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

load_dotenv()

DRIVER_PATH = os.getenv('DRIVER_PATH')
LOGIN_PAGE = os.getenv('LOGIN_PAGE')


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = LOGIN_PAGE
        self.call_button_locator = (By.CSS_SELECTOR, "button[value='OUTGOING_CALL']")
        self.sms_button_locator = (By.CSS_SELECTOR, "button[value='SMS']")
        self.back_button_locator = (By.CSS_SELECTOR, "button.secondary")
        self.phone_input_locator = (By.CSS_SELECTOR, "input[name='phone']")

    def open(self):
        self.driver.get(self.url)

    def click_call_button(self):
        self.driver.find_element(*self.call_button_locator).click()

    def click_sms_button(self):
        self.driver.find_element(*self.sms_button_locator).click()

    def click_back_button(self):
        self.driver.find_element(*self.back_button_locator).click()

    def is_phone_input_present(self):
        return self.driver.find_element(*self.phone_input_locator).is_displayed()


if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver_service = ChromeService(executable_path=DRIVER_PATH)
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_call_button()
        print(login_page.is_phone_input_present())
        time.sleep(1)
        login_page.click_back_button()
        time.sleep(1)
    finally:
        driver.quit()
