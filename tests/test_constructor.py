from selenium.webdriver.common.by import By
from locators import MainPageLocators


class TestConstructor:
    def test_constructor_page_insides_button_pressed_true(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site/")

        chrome_driver.find_element(By.XPATH, MainPageLocators.INSIDES_BUTTON).click()

        button = chrome_driver.find_element(By.XPATH, MainPageLocators.SECTION_INSIDES)

        assert "tab_tab_type_current__2BEPc" in button.get_attribute("class")

    def test_constructor_page_buns_button_pressed_true(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site/")
        chrome_driver.find_element(By.XPATH, MainPageLocators.SAUCES_BUTTON).click()
        chrome_driver.find_element(By.XPATH, MainPageLocators.PANS_BUTTON).click()

        button = chrome_driver.find_element(By.XPATH, MainPageLocators.SECTION_PANS)

        assert "tab_tab_type_current__2BEPc" in button.get_attribute("class")

    def test_constructor_page_sauces_button_pressed_true(self, chrome_driver):
        chrome_driver.get("https://stellarburgers.nomoreparties.site/")

        chrome_driver.find_element(By.XPATH, MainPageLocators.SAUCES_BUTTON).click()

        button = chrome_driver.find_element(By.XPATH, MainPageLocators.SECTION_SAUCE)

        assert "tab_tab_type_current__2BEPc" in button.get_attribute("class")
