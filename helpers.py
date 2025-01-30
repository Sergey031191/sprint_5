import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, LoginPageLocators

user_login = "smth" + str(random.randint(0, 999))
user_email = user_login + "@milo.org"
user_password = "qwerty"

MAIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/"
REGISTER_PAGE_URL = "https://stellarburgers.nomoreparties.site/register"
PASSWORD_RESTORE_PAGE_URL = "https://stellarburgers.nomoreparties.site/forgot-password"
LOGIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/login"
USER_ACCOUNT_PAGE = "https://stellarburgers.nomoreparties.site/account/profile"


def login(chrome_driver):
    WebDriverWait(chrome_driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, LoginPageLocators.LOGIN_BUTTON)))

    chrome_driver.find_element(By.NAME, LoginPageLocators.NAME_FIELD).send_keys("sergey_qa_17@pochta.ru")
    chrome_driver.find_element(By.NAME, LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")
    chrome_driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(chrome_driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, MainPageLocators.ENTER_ACCOUNT_BUTTON)))
