import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, UserAccountPageLocators
from helpers import login, MAIN_PAGE_URL


@pytest.fixture()
def chrome_driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def chrome_driver_logged():
    chrome_driver_logged = webdriver.Chrome()
    chrome_driver_logged.get(MAIN_PAGE_URL)
    WebDriverWait(chrome_driver_logged, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, MainPageLocators.USER_ACCOUNT_BUTTON)))

    chrome_driver_logged.find_element(By.XPATH, MainPageLocators.USER_ACCOUNT_BUTTON).click()

    login(chrome_driver_logged)

    chrome_driver_logged.find_element(By.XPATH, MainPageLocators.USER_ACCOUNT_BUTTON).click()

    WebDriverWait(chrome_driver_logged, 5).until(
        expected_conditions.visibility_of_element_located((
            By.XPATH, UserAccountPageLocators.SAVE_BUTTON)))

    yield chrome_driver_logged

    chrome_driver_logged.quit()
