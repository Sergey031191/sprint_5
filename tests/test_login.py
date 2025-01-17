from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import login
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, PasswordRestorePageLocators


def test_login_by_enter_account_button_valid_user_data_true(chrome_driver):

    chrome_driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(chrome_driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, MainPageLocators.ENTER_ACCOUNT_BUTTON)))

    chrome_driver.find_element(By.CSS_SELECTOR, MainPageLocators.ENTER_ACCOUNT_BUTTON).click()

    login(chrome_driver)

    assert chrome_driver.current_url == "https://stellarburgers.nomoreparties.site/"


def test_login_by_user_account_button_valid_user_data_true(chrome_driver):

    chrome_driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(chrome_driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, MainPageLocators.USER_ACCOUNT_BUTTON)))

    chrome_driver.find_element(By.XPATH, MainPageLocators.USER_ACCOUNT_BUTTON).click()

    login(chrome_driver)

    assert chrome_driver.current_url == "https://stellarburgers.nomoreparties.site/"


def test_login_from_registration_page_valid_user_data_true(chrome_driver):

    chrome_driver.get("https://stellarburgers.nomoreparties.site/register")

    WebDriverWait(chrome_driver, 5).until(
        expected_conditions.text_to_be_present_in_element((
            By.XPATH, RegistrationPageLocators.REGISTER_BUTTON), "Зарегистрироваться"))

    chrome_driver.find_element(By.CLASS_NAME, RegistrationPageLocators.LOGIN_BUTTON).click()

    login(chrome_driver)

    assert chrome_driver.current_url == "https://stellarburgers.nomoreparties.site/"


def test_login_from_password_restore_page_valid_user_data_true(chrome_driver):

    chrome_driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    WebDriverWait(chrome_driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, PasswordRestorePageLocators.LOGIN_BUTTON)))

    chrome_driver.find_element(By.XPATH, PasswordRestorePageLocators.LOGIN_BUTTON).click()

    login(chrome_driver)

    assert chrome_driver.current_url == "https://stellarburgers.nomoreparties.site/"

