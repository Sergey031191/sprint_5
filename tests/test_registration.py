from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationPageLocators, LoginPageLocators
from helpers import user_login, user_password, user_email, REGISTER_PAGE_URL, LOGIN_PAGE_URL


class TestRegistration:
    def test_registration_correct_inputs_true(self, chrome_driver):
        chrome_driver.get(REGISTER_PAGE_URL)

        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.text_to_be_present_in_element((
                By.XPATH, RegistrationPageLocators.REGISTER_BUTTON), "Зарегистрироваться"))

        chrome_driver.find_element(By.XPATH, RegistrationPageLocators.NAME_INPUT).send_keys(user_login)
        chrome_driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_INPUT).send_keys(user_email)
        chrome_driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_INPUT).send_keys(user_password)

        chrome_driver.find_element(By.XPATH, RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.text_to_be_present_in_element((
                By.XPATH, LoginPageLocators.LOGIN_BUTTON), "Войти"))

        assert chrome_driver.current_url == LOGIN_PAGE_URL

    def test_registration_wrong_password_input_true(self, chrome_driver):
        chrome_driver.get(REGISTER_PAGE_URL)

        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.text_to_be_present_in_element((
                By.XPATH, RegistrationPageLocators.REGISTER_BUTTON), "Зарегистрироваться"))

        chrome_driver.find_element(By.XPATH, RegistrationPageLocators.NAME_INPUT).send_keys("some_kitty_cat_6")
        chrome_driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_INPUT).send_keys(
            "some_kitty_cat_66@maim.com")
        chrome_driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_INPUT).send_keys("Sar")

        chrome_driver.find_element(By.XPATH, RegistrationPageLocators.REGISTER_BUTTON).click()

        popup_text = chrome_driver.find_element(By.CSS_SELECTOR, RegistrationPageLocators.WRONG_PASSWORD_POPUP).text

        assert popup_text == "Некорректный пароль"
