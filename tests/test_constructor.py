from selenium.webdriver.common.by import By
from locators import MainPageLocators


def test_constructor_page_insides_button_pressed_true(chrome_driver):
    chrome_driver.get("https://stellarburgers.nomoreparties.site/")

    chrome_driver.find_element(By.XPATH, MainPageLocators.insides_button).click()

    button = chrome_driver.find_element(By.XPATH, ".//div[@style='display: flex;']/div[3]")

    assert "tab_tab_type_current__2BEPc" in button.get_attribute("class")


def test_constructor_page_buns_button_pressed_true(chrome_driver):
    chrome_driver.get("https://stellarburgers.nomoreparties.site/")
    chrome_driver.find_element(By.XPATH, MainPageLocators.sauces_button).click()
    chrome_driver.find_element(By.XPATH, MainPageLocators.pans_button).click()

    button = chrome_driver.find_element(By.XPATH, ".//div[@style='display: flex;']/div[1]")

    assert "tab_tab_type_current__2BEPc" in button.get_attribute("class")


def test_constructor_page_sauces_button_pressed_true(chrome_driver):
    chrome_driver.get("https://stellarburgers.nomoreparties.site/")

    chrome_driver.find_element(By.XPATH, MainPageLocators.sauces_button).click()

    button = chrome_driver.find_element(By.XPATH, ".//div[@style='display: flex;']/div[2]")

    assert "tab_tab_type_current__2BEPc" in button.get_attribute("class")
