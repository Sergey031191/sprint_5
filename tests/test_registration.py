from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationPageLocators, LoginPageLocators
from helpers import user_login, user_password, user_email


def test_registration_correct_inputs_true(chrome_driver):
    chrome_driver.get("https://stellarburgers.nomoreparties.site/register")

    WebDriverWait(chrome_driver, 5).until(
        expected_conditions.text_to_be_present_in_element((
            By.XPATH, RegistrationPageLocators.register), "Зарегистрироваться"))

    chrome_driver.find_element(By.XPATH, RegistrationPageLocators.name).send_keys(user_login)
    chrome_driver.find_element(By.XPATH, RegistrationPageLocators.email).send_keys(user_email)
    chrome_driver.find_element(By.XPATH, RegistrationPageLocators.password).send_keys(user_password)

    chrome_driver.find_element(By.XPATH, RegistrationPageLocators.register).click()

    WebDriverWait(chrome_driver, 5).until(
        expected_conditions.text_to_be_present_in_element((
            By.XPATH, LoginPageLocators.login), "Войти"))

    assert chrome_driver.current_url == "https://stellarburgers.nomoreparties.site/login"


def test_registration_wrong_password_input_true(chrome_driver):
    chrome_driver.get("https://stellarburgers.nomoreparties.site/register")

    WebDriverWait(chrome_driver, 5).until(
        expected_conditions.text_to_be_present_in_element((
            By.XPATH, RegistrationPageLocators.register), "Зарегистрироваться"))

    chrome_driver.find_element(By.XPATH, RegistrationPageLocators.name).send_keys("some_kitty_cat_6")
    chrome_driver.find_element(By.XPATH, RegistrationPageLocators.email).send_keys("some_kitty_cat_66@maim.com")
    chrome_driver.find_element(By.XPATH, RegistrationPageLocators.password).send_keys("Sar")

    chrome_driver.find_element(By.XPATH, RegistrationPageLocators.register).click()

    popup_text = chrome_driver.find_element(By.CSS_SELECTOR, RegistrationPageLocators.wrong_password).text

    assert popup_text == "Некорректный пароль"



