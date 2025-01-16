import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, LoginPageLocators

user_login = "smth" + str(random.randint(0, 999))
user_email = user_login + "@milo.org"
user_password = "qwerty"


def login(chrome_driver):
    WebDriverWait(chrome_driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, LoginPageLocators.login)))

    chrome_driver.find_element(By.NAME, LoginPageLocators.name_field).send_keys("sergey_qa_17@pochta.ru")
    chrome_driver.find_element(By.NAME, LoginPageLocators.password_field).send_keys("qwerty")
    chrome_driver.find_element(By.XPATH, LoginPageLocators.login).click()

    WebDriverWait(chrome_driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, MainPageLocators.enter_account)))
