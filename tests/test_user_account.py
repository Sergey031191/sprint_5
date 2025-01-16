from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, UserAccountPageLocators, LoginPageLocators


def test_user_account_button_check_when_logged(chrome_driver_logged):

    chrome_driver_logged.find_element(By.XPATH, MainPageLocators.user_account).click()

    WebDriverWait(chrome_driver_logged, 5).until(
        expected_conditions.visibility_of_element_located((
            By.XPATH, UserAccountPageLocators.save_button)))

    assert chrome_driver_logged.current_url == "https://stellarburgers.nomoreparties.site/account/profile"


def test_open_constructor_from_user_account_page_true(chrome_driver_logged):

    chrome_driver_logged.find_element(By.XPATH, MainPageLocators.user_account).click()

    WebDriverWait(chrome_driver_logged, 5).until(
        expected_conditions.visibility_of_element_located((
            By.XPATH, UserAccountPageLocators.save_button)))

    chrome_driver_logged.find_element(By.XPATH, UserAccountPageLocators.constructor).click()

    WebDriverWait(chrome_driver_logged, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, MainPageLocators.user_account)))

    assert chrome_driver_logged.current_url == "https://stellarburgers.nomoreparties.site/"


def test_user_logout_from_account_page_true(chrome_driver_logged):
    chrome_driver_logged.find_element(By.XPATH, MainPageLocators.user_account).click()

    WebDriverWait(chrome_driver_logged, 5).until(
        expected_conditions.visibility_of_element_located((
            By.XPATH, UserAccountPageLocators.save_button)))

    chrome_driver_logged.find_element(By.XPATH, UserAccountPageLocators.exit_button).click()

    WebDriverWait(chrome_driver_logged, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, LoginPageLocators.login)))

    assert chrome_driver_logged.current_url == "https://stellarburgers.nomoreparties.site/login"