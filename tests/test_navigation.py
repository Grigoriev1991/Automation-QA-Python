from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage


def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))


def test_open_main_page(main_page: MainPage):
    main_page.open()
    wait_for_element(main_page.driver, main_page.login_button)
    assert main_page.get_login_button().is_displayed(), "Главная страница не открылась"


def test_navigation_to_login_page(main_page: MainPage, login_page: LoginPage):
    main_page.open()
    main_page.click_login()
    wait_for_element(login_page.driver, login_page.call_button_locator)
    assert login_page.driver.find_element(*login_page.call_button_locator).is_displayed(), "Не найдена кнопка авторизации по звонку"
    assert login_page.driver.find_element(*login_page.sms_button_locator).is_displayed(), "Не найдена кнопка авторизации по СМС"


def test_click_call_button(login_page: LoginPage):
    login_page.open()
    wait_for_element(login_page.driver, login_page.call_button_locator)
    login_page.click_call_button()
    wait_for_element(login_page.driver, login_page.phone_input_locator)
    assert login_page.is_phone_input_present(), "Страница регистрации по звонку не открылась или поле ввода телефона не найдено"


def test_click_sms_button(login_page: LoginPage):
    login_page.open()
    wait_for_element(login_page.driver, login_page.sms_button_locator)
    login_page.click_sms_button()
    wait_for_element(login_page.driver, login_page.phone_input_locator)
    assert login_page.is_phone_input_present(), "Страница регистраци по SMS не открылась или поле ввода телефона не найдено"
